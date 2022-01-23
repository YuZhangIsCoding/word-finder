# word-finder

This is the repo for the word-finder project

Setting up:
```shell
pip install pipenv
pipenv shell
pipenv install --dev
```

Usage:
```shell
Usage: main.py [OPTIONS] PATTERN

Options:
  --version             Show the version and exit.
  --exact               Match the pattern exactly
  -l, --length INTEGER  The length of the word
  --limit INTEGER       Limit the number of the output words
  -c, --corpus TEXT     Choose the corpus from ['nltk_corpus']
  --cache PATH          Cache location
  --help                Show this message and exit.
```

Example:
```shell
./main.py "*in*e" --limit -1 --exact
```
