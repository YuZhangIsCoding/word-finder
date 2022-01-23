#!/usr/bin/env python
import functools
import re
from collections import Counter
from typing import Callable, Iterable, Iterator

import click

import word_finder.corpus as corpus_module
from word_finder.log import get_logger

from .__init__ import __version__

LOGGER = get_logger(__name__)


def search(exact: bool) -> Callable[[Iterator[str], str, int], Iterator[str]]:
    """Search the words with given pattern"""

    @functools.wraps(search)
    def exact_search(words: Iterable[str], pattern: str, length: int) -> Iterator[str]:
        """The word has to match the letter at the exact position"""
        if 0 < length < len(pattern):
            raise ValueError(
                "The specified word length is smaller than the length of the pattern"
            )
        pattern_lower = pattern.lower()
        wild_string = re.sub("[^a-z]", "*", pattern_lower).ljust(
            max(len(pattern), length), "*"
        )
        LOGGER.info(f"Searching words with the exact pattern of `{wild_string}`")
        pattern_indices = [
            idx for idx, letter in enumerate(pattern_lower) if letter.isalpha()
        ]
        for word in words:
            if 0 < length != len(word):
                continue
            if all(
                idx < len(word) and pattern_lower[idx] == word[idx]
                for idx in pattern_indices
            ):
                yield word

    @functools.wraps(search)
    def simple_search(words: Iterable, pattern: str, length: int) -> Iterator[str]:
        """The word has all of the letters in the given pattern"""
        pattern_counter = Counter(
            letter for letter in pattern.lower() if letter.isalpha()
        )
        pattern_string = ", ".join(
            [f"{cnt} of {key}" for key, cnt in pattern_counter.items()]
        )
        LOGGER.info(f"Searching words with at least `{pattern_string}`")
        for word in words:
            if 0 < length != len(word):
                continue
            word_counter = Counter(word)
            for letter, count in pattern_counter.items():
                if count > word_counter[letter]:
                    break
            else:
                yield word

    if exact:
        return exact_search
    else:
        return simple_search


@click.command()
@click.version_option(version=__version__)
@click.argument("pattern", type=str)
@click.option(
    "--exact", type=bool, default=False, is_flag=True, help="Match the pattern exactly"
)
@click.option("-l", "--length", type=int, default=5, help="The length of the word")
@click.option(
    "--limit", type=int, default=5, help="Limit the number of the output words"
)
@click.option(
    "-c",
    "--corpus",
    type=str,
    default="nltk_corpus",
    help=f"Choose the corpus from {corpus_module.__all__}",
)
@click.option("--cache", type=click.Path(), default=".cache", help="Cache location")
@click.option("--cache-file", type=click.Path(), help="Cached file name")
@click.option(
    "--clear",
    type=bool,
    is_flag=True,
    default=False,
    help="Clear the previous cached file",
)
@click.option(
    "--url",
    type=str,
    default="http://www.mieliestronk.com/corncob_lowercase.txt",
    help="Url to the text corpus",
)
def main(pattern, exact, length, limit, corpus, cache, cache_file, clear, url):
    all_words = corpus_module.__dict__[corpus].read_words(
        cache=cache,
        cache_file=cache_file,
        clear=clear,
        url=url,
    )

    for i, word in enumerate(search(exact)(all_words, pattern, length)):
        if limit <= 0 or i < limit:
            LOGGER.info(f"Candidate {i+1}: {word}")


if __name__ == "__main__":
    main()
