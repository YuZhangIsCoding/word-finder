# word-finder

This is the repo for the word-finder project

Recently, a lot of my friends are super into the game [wordle](https://www.powerlanguage.co.uk/wordle/). However, as a
non-native English speaker, and not super talented in language, I sometimes find it exhausting to think of a word given
the hint from the previous tries. Thus, the purpose of this repo is to help me to put together a pool of candidates
given a pattern;)

Set the dev env:
```shell
pip install pipenv
pip install pre-commit
cd <repo root>
pre-commit install
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
-> % ./main.py "*in*e" --limit -1 --exact
[nltk_data] Downloading package words to .cache...
[nltk_data]   Package words is already up-to-date!
2022-01-22 23:28:05,650 - word_finder.corpus.nltk_corpus - INFO - The corpus has 234377 unique words
2022-01-22 23:28:05,650 - word_finder.__main__ - INFO - Searching words with the exact pattern of `*in*e`
2022-01-22 23:28:05,655 - word_finder.__main__ - INFO - Candidate 1: hinge
2022-01-22 23:28:05,656 - word_finder.__main__ - INFO - Candidate 2: pinte
2022-01-22 23:28:05,656 - word_finder.__main__ - INFO - Candidate 3: binge
2022-01-22 23:28:05,657 - word_finder.__main__ - INFO - Candidate 4: singe
2022-01-22 23:28:05,661 - word_finder.__main__ - INFO - Candidate 5: tinge
2022-01-22 23:28:05,664 - word_finder.__main__ - INFO - Candidate 6: since
2022-01-22 23:28:05,664 - word_finder.__main__ - INFO - Candidate 7: ringe
2022-01-22 23:28:05,665 - word_finder.__main__ - INFO - Candidate 8: mince
2022-01-22 23:28:05,668 - word_finder.__main__ - INFO - Candidate 9: yince
2022-01-22 23:28:05,669 - word_finder.__main__ - INFO - Candidate 10: minge
2022-01-22 23:28:05,676 - word_finder.__main__ - INFO - Candidate 11: linge
2022-01-22 23:28:05,686 - word_finder.__main__ - INFO - Candidate 12: linje
2022-01-22 23:28:05,687 - word_finder.__main__ - INFO - Candidate 13: winze
2022-01-22 23:28:05,692 - word_finder.__main__ - INFO - Candidate 14: tinne
2022-01-22 23:28:05,694 - word_finder.__main__ - INFO - Candidate 15: sinae
2022-01-22 23:28:05,694 - word_finder.__main__ - INFO - Candidate 16: wince
2022-01-22 23:28:05,695 - word_finder.__main__ - INFO - Candidate 17: dinge
2022-01-22 23:28:05,699 - word_finder.__main__ - INFO - Candidate 18: rinse
2022-01-22 23:28:05,704 - word_finder.__main__ - INFO - Candidate 19: rinde
2022-01-22 23:28:05,711 - word_finder.__main__ - INFO - Candidate 20: vince
2022-01-22 23:28:05,713 - word_finder.__main__ - INFO - Candidate 21: linie
2022-01-22 23:28:05,718 - word_finder.__main__ - INFO - Candidate 22: linne
```
