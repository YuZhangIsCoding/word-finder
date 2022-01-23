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
  -c, --corpus TEXT     Choose the corpus from ['nltk_corpus', 'web']
  --cache PATH          Cache location
  --cache-file PATH     Cached file name
  --clear               Clear the previous cached file
  --url TEXT            Url to the text corpus
  --help                Show this message and exit.

```

Example:

* Search from `nltk_data`
```shell
-> % ./main.py "*in*e" --limit -1 --exact
2022-01-23 15:34:19,165 - word_finder.corpus.nltk_corpus - INFO - Reading words from `nltk_data`
2022-01-23 15:34:19,165 - word_finder.cache - INFO - Reading previous cached file: .cache/nltk_etl.cache=5df83c78ea58fa2f7eb87e8085bea10c.txt
2022-01-23 15:34:19,206 - word_finder.__main__ - INFO - Searching words with the exact pattern of `*in*e`
2022-01-23 15:34:19,207 - word_finder.__main__ - INFO - Candidate 1: dinge
2022-01-23 15:34:19,217 - word_finder.__main__ - INFO - Candidate 2: minge
2022-01-23 15:34:19,220 - word_finder.__main__ - INFO - Candidate 3: since
2022-01-23 15:34:19,221 - word_finder.__main__ - INFO - Candidate 4: sinae
2022-01-23 15:34:19,228 - word_finder.__main__ - INFO - Candidate 5: tinge
2022-01-23 15:34:19,231 - word_finder.__main__ - INFO - Candidate 6: hinge
2022-01-23 15:34:19,237 - word_finder.__main__ - INFO - Candidate 7: winze
2022-01-23 15:34:19,239 - word_finder.__main__ - INFO - Candidate 8: linie
2022-01-23 15:34:19,241 - word_finder.__main__ - INFO - Candidate 9: singe
2022-01-23 15:34:19,245 - word_finder.__main__ - INFO - Candidate 10: rinse
2022-01-23 15:34:19,246 - word_finder.__main__ - INFO - Candidate 11: wince
2022-01-23 15:34:19,247 - word_finder.__main__ - INFO - Candidate 12: ringe
2022-01-23 15:34:19,248 - word_finder.__main__ - INFO - Candidate 13: yince
2022-01-23 15:34:19,248 - word_finder.__main__ - INFO - Candidate 14: vince
2022-01-23 15:34:19,250 - word_finder.__main__ - INFO - Candidate 15: tinne
2022-01-23 15:34:19,255 - word_finder.__main__ - INFO - Candidate 16: binge
2022-01-23 15:34:19,256 - word_finder.__main__ - INFO - Candidate 17: linne
2022-01-23 15:34:19,257 - word_finder.__main__ - INFO - Candidate 18: mince
2022-01-23 15:34:19,257 - word_finder.__main__ - INFO - Candidate 19: linge
2022-01-23 15:34:19,258 - word_finder.__main__ - INFO - Candidate 20: rinde
2022-01-23 15:34:19,261 - word_finder.__main__ - INFO - Candidate 21: pinte
2022-01-23 15:34:19,263 - word_finder.__main__ - INFO - Candidate 22: linje
```
* Search from webpage
```shell
-> % ./main.py "*in*e" --limit -1 --exact -c web
2022-01-23 15:35:01,604 - word_finder.corpus.web - INFO - Reading the words from http://www.mieliestronk.com/corncob_lowercase.txt...
2022-01-23 15:35:01,605 - word_finder.cache - INFO - Reading previous cached file: .cache/web_etl.url=017e9289840f8e0b493049e6d66690a6.txt
2022-01-23 15:35:01,614 - word_finder.__main__ - INFO - Searching words with the exact pattern of `*in*e`
2022-01-23 15:35:01,616 - word_finder.__main__ - INFO - Candidate 1: binge
2022-01-23 15:35:01,617 - word_finder.__main__ - INFO - Candidate 2: hinge
2022-01-23 15:35:01,618 - word_finder.__main__ - INFO - Candidate 3: since
2022-01-23 15:35:01,620 - word_finder.__main__ - INFO - Candidate 4: wince
2022-01-23 15:35:01,621 - word_finder.__main__ - INFO - Candidate 5: rinse
2022-01-23 15:35:01,622 - word_finder.__main__ - INFO - Candidate 6: tinge
2022-01-23 15:35:01,623 - word_finder.__main__ - INFO - Candidate 7: minke
2022-01-23 15:35:01,624 - word_finder.__main__ - INFO - Candidate 8: singe
2022-01-23 15:35:01,625 - word_finder.__main__ - INFO - Candidate 9: mince
```
