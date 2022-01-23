from pathlib import Path
from typing import List, Union

import nltk
from nltk.corpus import words

from word_finder.log import get_logger

LOGGER = get_logger(__name__)


def read_words(cache: Union[str, Path]) -> List[str]:
    nltk.download("words", download_dir=cache)

    all_words = list(set(word.lower() for word in words.words()))
    LOGGER.info(f"The corpus has {len(all_words)} unique words")

    return all_words
