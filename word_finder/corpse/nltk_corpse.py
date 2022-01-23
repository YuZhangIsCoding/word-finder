import nltk
from nltk.corpus import words
from typing import Union, List
from pathlib import Path
from word_finder.log import get_logger


LOGGER = get_logger(__name__)


def read_words(cache: Union[str, Path]) -> List[str]:
    nltk.download("words", download_dir=cache)

    all_words = list(set(word.lower() for word in words.words()))
    LOGGER.info(f"The corpse has {len(all_words)} unique words")

    return all_words
