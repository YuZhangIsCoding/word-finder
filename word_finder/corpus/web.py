import re
from pathlib import Path
from typing import Iterable, List, Optional, Union

import requests

from word_finder.cache import cached_words
from word_finder.log import get_logger

LOGGER = get_logger(__name__)


def web_etl(url) -> List[str]:
    """Assume the url is a pure text webpage

    return a list of unique words from the webpage
    """

    response = requests.get(url)
    response.raise_for_status()

    words = list(
        set(
            word
            for line in response.text.split("\n")
            for word in re.split("[^a-z]", line.strip().lower())
        )
    )
    return words


def read_words(
    url: str,
    cache: Union[str, Path],
    cache_file: Optional[Union[str, Path]] = None,
    clear: bool = False,
    *args,
    **kwargs,
) -> Iterable[str]:
    """Read words from a webpage"""
    LOGGER.info(f"Reading the words from {url}...")
    return cached_words(web_etl, cache_file, cache, clear)(url)
