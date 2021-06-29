# Concentration Game

This is the final post-examination project of the Brookline High School [2020-2021 APCS-P](https://sites.google.com/psbma.org/david-petty/archive/2020-2021/apcsp) non-seniors. This codebase is a repository of [https://github.com/psb-2020-2021-apcsp/](https://github.com/psb-2020-2021-apcsp/) and was originally developed on [https://replit.com/@bhsapcsp2021/Concentration-Game](https://replit.com/@bhsapcsp2021/Concentration-Game).

## Description

**[Concentration Game](https://psb-2020-2021-apcsp.github.io/concentration-game)** is a concentration memory game involving standard playing cards. It is based on [Tkinter](https://docs.python.org/3/library/tkinter.html) and creates a grid of face-down cards in an approximate square. The object of the game is to flip over all matched pairs of cards. The possible number of pairs to match in the various games are: `(3, 6, 12, 14, 20, 24, 27, 30, 35, 42, 44, 48, 52)`. 

Score is determined... **HOW?**

## Modules

| File | Description |
| --- | --- |
| `src/app.py` | The main [Tkinter](https://docs.python.org/3/library/tkinter.html) GUI app. |
| `src/credit.py` | Module that implements the `Credit` widget. |
| `src/files.py` | Module that manages image file paths. |
| `src/game.py` | Module that implements the `Game` widget. |
| `src/gameplay.py` | Module that implements the gameplay [state machine](https://en.wikipedia.org/wiki/Mealy_machine). |
| `src/info.py` | Module that implements the `Info` widget. |
| `src/layout.py` | Module that calculates game card layouts. |
| `src/log.py` | Module that implements app [`logging`](https://docs.python.org/3/library/logging.html). |
| `src/main.py` | Module that initiates the app. |
| `src/score.py` | Module that implements game scoring. |
| `tests/test_layout.py` | Unit tests for `layout.py` (so far). |

### `app.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `credit.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `files.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `game.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `gameplay.py`

| Question | Description |
| --- | --- |
| What: | Module that implements the gameplay [state machine](https://en.wikipedia.org/wiki/Mealy_machine) (below). |
| API: | &bull; `fsm(signal=None)` &mdash; If `signal` is a `(row, column, )` tuple, then it represents a click of that card. If `signal` is `None`, then it represents a timeout. |
| Callbacks: | &bull; `get_id` &mdash; `get_id((row, column, ))` returns the *name* of the face image on button `(row, column, )` which will be the same for matching cards,<br>&bull; `show_back` &mdash; `show_back((row, column, ))` shows the card back image on button `(row, column, )`.<br>&bull; `show_face` &mdash; `show_face((row, column, ))` shows the card face image on button `(row, column, )`.<br>&bull; `start_delay` &mdash; `start_delay()` starts the incorrect-match delay, eventually invoking `fsm()` unless stopped.<br>&bull; `stop_delay` &mdash; `stop_delay()` stops any incorrect-match delays. |
| How: | &bull; How was the *what* implemented? [TK](https://en.wikipedia.org/wiki/To_come_(publishing)) |
| Why: | &bull; Why were the *what* and *how* choices made? [TK](https://en.wikipedia.org/wiki/To_come_(publishing))<br>&bull; What did I learn? [TK](https://en.wikipedia.org/wiki/To_come_(publishing)) |

![concentration state machine](./concentration-state-machine.png)

[Gliffy](https://gliffy.com) [source](https://go.gliffy.com/go/publish/13517385)

### `info.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `layout.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `log.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `main.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `score.py`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

Note: [This paper](http://eprints-dev5.cs.univie.ac.at/5522/1/2013-memory.pdf) indicates that, in 'the 1-player solitaire game, where the goal is to need as few moves as possible to collect all cards off the table, ...[we] prove that an optimal strategy needs less than 1.75 &times; n moves in expectation.' That may give us some insight into game timing or scoring.

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

### `tests/`

| Question | Description **TEMPLATE** |
| --- | --- |
| What: | Module that implements... |
| API: | &bull; `function` &mdash; |
| Callbacks: | &bull; `variable` &mdash;  |
| How: | &bull; How was the *what* implemented? |
| Why: | &bull; Why were the *what* and *how* choices made?<br>&bull; What did I learn? |

More [TK](https://en.wikipedia.org/wiki/To_come_(publishing)).

## TODO

Tasks for this project include:

- *This [documentation file](https://github.com/psb-2020-2021-apcsp/concentration-game/blob/main/README.md) should be completed*.
- In general, all code should follow [PEP-8](https://www.python.org/dev/peps/pep-0008/).
- Currently, the `Image` randomization takes place in `app.py` rather than `files.py`. There are two issues:
  - `Image`s are loaded with every change of game geometry (including the card back). It seems they should be loaded just once, but each time they must be resized &mdash; would that mean their quality would degrade with each game?
  - Should the `Image` randomization take place in `files.py`?
- Scoring simply keeps track of good and bad guesses. Nothing is done to detect winning, nor is anything done with a maximum time for losing.
- Can we make this into a two-player game?
- Unit tests (using [`pytest`](https://docs.pytest.org/)) for *all* functions. (We has started using `unittest`).
- Add some [command-line options](https://docs.python.org/3/library/argparse.html) (perhaps initial game size, logging level, *etc.*?).
- Classes? Should we encapsulate everything and make it object-oriented?
- Make this a runnable app? (How?)
- Update `replit.sh` to selectively use `pip3` and run all unit tests.
- *So much more!* (See our [notes](https://drive.google.com/file/d/1UhX4aK-9mBqioveEm5JWuqGeYFfpsKQS/view).)

[&#128279; permalink](https://psb-2020-2021-apcsp.github.io/concentration-game) and [&#128297; repository](https://github.com/psb-2020-2021-apcsp/concentration-game) for this page.
