# Concentration Game

This is the final post-examination project of the Brookline High School [2020-2021 APCS-P](https://sites.google.com/psbma.org/david-petty/archive/2020-2021/apcsp) non-seniors. This codebase was originally developed on [https://replit.com/@bhsapcsp2021/Concentration-Game](https://replit.com/@bhsapcsp2021/Concentration-Game).

## Description

**DESCRIPTION HERE:** This is a concentration memory game...

## TODO

Tasks for this project include:

- We need to give credit for the card images (source:[http://acbl.mybigcommerce.com/52-playing-cards/](http://acbl.mybigcommerce.com/52-playing-cards/)) &mdash; and we need a joker card image & card back image.
- User interface:
  - Managing user input for things like the number of card pairs.
  - Labels for score, timers, *etc.*.
- Data structures:
  - Create a dictionary of filenames mapped to `Image`s using [`os.walk`](https://docs.python.org/3/library/os.html#os.walk).
  - Manage the positioning of random non-repeating pairs in a grid matching the button grid (and adding the images to the buttons).
  - Keeping track of matched pairs, score, timing, *etc.*.
- Game-play [state machine](https://en.wikipedia.org/wiki/Mealy_machine).
- Timing (using [`threading`](https://docs.python.org/3/library/threading.html)), because part of the game-play state machine involves delaying on a wrong answer.
- Unit tests (using [`unittest`](https://docs.python.org/3/library/unittest.html)) for *all* functions.
- Classes? Should we encapsulate everything and make it object-oriented?
- *So much more!* (See our [notes](https://drive.google.com/file/d/1UhX4aK-9mBqioveEm5JWuqGeYFfpsKQS/view).)

<hr>

[&#128279; permalink](https://psb-2020-2021-apcsp.github.io/concentration-game) and [&#128297; repository](https://github.com/psb-2020-2021-apcsp/concentration-game) for this page.
