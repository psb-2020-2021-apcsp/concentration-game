# Concentration Game

This is the final post-examination project of the Brookline High School [2020-2021 APCS-P](https://sites.google.com/psbma.org/david-petty/archive/2020-2021/apcsp) non-seniors. This codebase was originally developed on [https://replit.com/@bhsapcsp2021/Concentration-Game](https://replit.com/@bhsapcsp2021/Concentration-Game).

## Description

This is a concentration memory game involving standard playing cards. It is based on [Tkinter](https://docs.python.org/3/library/tkinter.html) and creates a grid of face-down cards in an approximate square. The possible number of pairs to match in the various games are: `(3, 6, 12, 14, 20, 24, 27, 30, 35, 42, 44, 48, 52)`. 

Score is determined... **HOW?**

## Modules

| File | Description |
| --- | --- |
| `src/app.py` | This is the main [Tkinter](https://docs.python.org/3/library/tkinter.html) GUI app. |
| `src/files.py` | Module that... |
| `src/gameplay.py` | Module that... |
| `src/layout.py` | Module that... |
| `src/log.py` | Module that... |
| `src/main.py` | Module that... |
| `src/timer.py` | Module that... |
| `src/unittest.py` | Module that... |
| `tests/test_layout.py` | Unit tests for `layout.py`. |

## TODO

Tasks for this project include:

- *This [documentation file](https://github.com/psb-2020-2021-apcsp/concentration-game/blob/main/README.md) should be completed*.
- In general, all code should follow [PEP-8](https://www.python.org/dev/peps/pep-0008/).
- We should create a credit frame with the [repo link](https://github.com/psb-2020-2021-apcsp/concentration-game) and the [card image](http://acbl.mybigcommerce.com/52-playing-cards/) link at the bottom of the main `Frame`. If we follow [this](https://stackoverflow.com/a/23482749), we should be able to make the credits clickable.
- Currently, the `Image` randomization takes place in `app.py` rather than `files.py`. There are two issues:
  - `Image`s are loaded with every change of game geometry. They should be loaded just once.
  - Should the `Image` randomization take place in `files.py`?
- The game-play [state machine](https://en.wikipedia.org/wiki/Mealy_machine) should be documented with corrections. 
- Also, **because `fsm` is invoked from different threads, it is possible to get into the wrong state with no way out**. So, either handle clicks waiting for a timeout, or synchronize `fsm`.
- Scoring simply keeps track of matches. Nothing is done to detect winning, nor is anything done with a maximum time for losing.
- Unit tests (using [`pytest`](https://docs.pytest.org/)) for *all* functions. (We has started using `unittest`).
- Classes? Should we encapsulate everything and make it object-oriented?
- *So much more!* (See our [notes](https://drive.google.com/file/d/1UhX4aK-9mBqioveEm5JWuqGeYFfpsKQS/view).)

[&#128279; permalink](https://psb-2020-2021-apcsp.github.io/concentration-game) and [&#128297; repository](https://github.com/psb-2020-2021-apcsp/concentration-game) for this page.
