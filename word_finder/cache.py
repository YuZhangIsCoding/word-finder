import functools
import hashlib
import inspect
import json
from pathlib import Path
from typing import Callable, Iterable, Optional, Union

from word_finder.log import get_logger

LOGGER = get_logger(__name__)


def md5(string: str) -> str:
    """MD5 hashing of a given string"""
    return hashlib.md5(string.encode()).hexdigest()


def get_or_create_cache(cache: Optional[Union[str, Path]]) -> Path:
    """Given a cache dir, create the dir if not exists and return the path"""
    cache_path = Path(cache) if cache else Path.cwd() / ".cache"
    if not cache_path.is_dir():
        cache_path.mkdir()
        LOGGER.info(f"Create a local cache folder: {cache_path}")
    return cache_path


def cached_words(
    etl_func: Callable[..., Iterable[str]],
    file_name: Optional[str] = None,
    cache: Optional[Union[str, Path]] = None,
    clear: bool = False,
    follow_wrapped: bool = False,
) -> Callable[..., Iterable[str]]:
    """Check if a file exists in the local cache.
    If it does, load it and return the words.
    Otherwise call the etl function to get the data and cache it to a local file.
    """

    @functools.wraps(etl_func)
    def wrapped(*args, **kwargs) -> Iterable[str]:
        if file_name:
            resolved_file_name = file_name
        else:
            all_args = []
            sig = inspect.signature(etl_func, follow_wrapped=follow_wrapped).parameters
            for i, name in enumerate(sig):
                if i < len(args):
                    all_args.append(f"{name}={md5(args[i])}")
                elif name in kwargs:
                    all_args.append(f"{name}={md5(kwargs[name])}")
                else:
                    all_args.append(f"{name}={md5(sig[name].default)}")
            resolved_file_name = etl_func.__name__ + "." + "__".join(all_args) + ".txt"

        cache_path = get_or_create_cache(cache)
        file_path = cache_path / resolved_file_name

        if clear and file_path.is_file():
            file_path.unlink()
            LOGGER.info(f"Clear previous cached file: {file_path}")

        if file_path.is_file():
            LOGGER.info(f"Reading previous cached file: {file_path}")
            with open(file_path) as f:
                return json.load(f)
        else:
            data = etl_func(*args, **kwargs)
            with open(file_path, "w") as f:
                json.dump(data, f)
            LOGGER.info(f"Cached the data as: {file_path}")
            return data

    return wrapped
