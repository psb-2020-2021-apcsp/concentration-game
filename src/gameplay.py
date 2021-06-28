#!/usr/bin/env python3
#
# gameplay.py
#
import log, score

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Implement the finite state machine for game play.
"""

logger = log.log(__name__)  # initialize logger

# Initialize module data.
state, first, second = 0, None, None
# Callbacks for show_back, show_face, get_id, echo w/ defaults.
show = lambda f, s: logger.info(f"{f}({s})")
delay = lambda s: logger.info(f"{s}")
show_back, show_face = lambda s: show('back', s), lambda s: show('frnt', s),
get_id = lambda s: [ f"pyimage{s[0]}", f"pyimage{s[0]}", ][s[1]]
start_delay, stop_delay = lambda: delay(f"start..."), lambda: delay(f"stop...")

def reset():
    global state, first, second
    state, first, second = 0, None, None

def fsm(signal=None):
    """Perform one step of the game-play FSM by processing signal.
    - If signal is a (row, column, ) tuple, then it represents a click
    of that card.
    - If signal is None, then it represents a timeout.
    TODO: a bit of a kludge, but workable for one oddball signal."""
    # Remember state and clicked values.
    global state, first, second
    states = [ 'start', 'clicked', 'wait', ]
    logger.info(f"start: {states[state]} {signal} ({first} {second})")

    if state == 0:      # start - not yet clicked
        if signal is None:
            state = 0   # start
        if signal is not None and score.matched(get_id(signal)):
            state = 0   # start
        if signal is not None and not score.matched(get_id(signal)):
            first = signal
            show_face(signal)
            state = 1   # clicked
    elif state == 1:    # clicked - clicked once
        if signal is None:
            state = 1   # clicked
        if signal is not None and score.matched(get_id(signal)) or signal == first:
            state = 1   # clicked
        if signal is not None and not score.matched(get_id(signal)) and signal != first:
            show_face(signal)
            second = signal
            logger.info(f"'{get_id(first)}' "
                        f"{'=' if get_id(first) == get_id(second) else '!'}= "
                        f"'{get_id(second)}'")
            if get_id(first) == get_id(second):
                score.score(get_id(signal))
                # Reinitialize first and second to clarify logging.
                first, second = None, None
                state = 0   # start
            else:
                score.score()
                start_delay()
                state = 2   # wait
    elif state == 2:    # wait - clicked twice and failed
        if signal is None:
            show_back(first)
            show_back(second)
            # Reinitialize first and second to clarify logging.
            first, second = None, None
            state = 0   # start
        if signal is not None and score.matched(get_id(signal)):
            state = 2   # wait
        if signal is not None and not score.matched(get_id(signal)):
            stop_delay()
            show_back(first)
            show_back(second)
            # Reinitialize first and second to clarify logging.
            first, second = None, None
            first = signal
            show_face(signal)
            state = 1   # clicked
    logger.info(f"  end: {states[state]} {signal} ({first} {second})")

if __name__ == "__main__":
    import time
    reset()

    # timeout
    fsm()

    # click same card twice, then correct pair
    fsm((0, 0,))
    fsm((0, 0,))
    fsm((0, 1,))

    # click incorrect pair
    fsm((1, 0,))
    fsm((2, 0,))
    logger.info('sleeping 3s...')
    time.sleep(3)

    # click correct pair
    fsm((1, 0,))
    fsm((1, 1,))

    # click correct pair, again
    fsm((1, 0,))
    fsm((1, 1,))
