import tempfile
from pathlib import Path
from typing import Iterable, List, Optional, Union

import nltk
from nltk.corpus import words

from word_finder.cache import cached_words, get_or_create_cache
from word_finder.log import get_logger

LOGGER = get_logger(__name__)


def nltk_etl(cache: Optional[Union[str, Path]] = None) -> List[str]:
    """Pull down the nltk data to a tmp dir and return the unique words"""
    cache_path = get_or_create_cache(cache)
    tmp_dir = tempfile.TemporaryDirectory(dir=cache_path)

    nltk.download("words", download_dir=tmp_dir.name)

    all_words = list(set(word.lower() for word in words.words()))
    LOGGER.info(f"The corpus has {len(all_words)} unique words")

    tmp_dir.cleanup()
    return all_words


def read_words(
    cache: Union[str, Path],
    cache_file: Optional[Union[str, Path]] = None,
    clear: bool = False,
    *args,
    **kwargs,
) -> Iterable[str]:
    """Read the words from nltk_data"""
    LOGGER.info("Reading words from `nltk_data`")
    return cached_words(nltk_etl, cache_file, cache, clear)(cache)
