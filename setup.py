import json
import os
from datetime import datetime

from setuptools import find_packages, setup


def _get_version_suffix():
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    commit = os.environ.get("GIT_COMMIT", "unknown")[:6]
    _write_meta({"commit": commit})
    return (
        ""
        if os.environ.get("RELEASE", "").lower() == "true"
        else f"-dev{timestamp}+{commit}"
    )


def _write_meta(data):
    directory = os.path.dirname(__file__)
    meta_path = os.path.join(directory, __name__, "meta.json")
    with open(meta_path, "w") as f:
        json.dump(data, f)


__name__ = "word_finder"
__version__ = f"0.2.0{_get_version_suffix()}"

setup(
    install_requires=[
        "click==8.0.3",
        "importlib-metadata==4.10.1; python_version < '3.8'",
        "joblib==1.1.0; python_version >= '3.6'",
        "nltk==3.6.7",
        "regex==2022.1.18",
        "tqdm==4.62.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "typing-extensions==4.0.1; python_version < '3.8'",
        "zipp==3.7.0; python_version >= '3.7'",
    ],
    name="word_finder",
    verion="0.1.0",
    author="Yu Zhang",
    author_email="YuZhang23333@gmail.com",
    description="This is a repo to find English words given key letters",
    packages=find_packages(exclude=["tests.*", "tests", "*.tests"]),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["word_finder=word_finder.__main__:main"]},
)
