import logging
import os
from typing import Optional

_LOGLEVEL = os.environ.get("LOGLEVEL", logging.INFO)
logging.basicConfig(
    level=_LOGLEVEL, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    return logging.getLogger(name)
