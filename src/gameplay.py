#!/usr/bin/env python3
#
# gameplay.py
#
import log, timer

"""
Implement the finite state machine for game play.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

logger = log.log(__name__)  # initialize logger

# Initialize module data.
state, first, second, correct = 0, None, None, list()
# Callbacks for show_back, show_face, get_id, echo w/ defaults.
show_back, show_face, get_id, echo = logger.info, logger.info, \
    lambda id: [ f"pyimage{id[0]}", f"pyimage{id[0]}", ][id[1]], logger.info

def reset():
    global state, first, second, correct
    state, first, second, correct = 0, None, None, list()

def fsm(signal=None):
    """Perform one step of the game-play FSM by processing signal.
    - If signal is a (row, column, ) tuple, then it represents a click
    of that card.
    - If signal is None, then it represents a timeout.
    TODO: a bit of a kludge, but workable for one oddball signal."""
    # Remember state and clicked values.
    global state, first, second, correct
    states = [ 'start', 'clicked', 'wait', ]
    logger.info(f"  start: {states[state]} {signal} ({first} {second})")

    if state == 0:      # start - not yet clicked
        if signal is None:
            state = 0   # start
        if signal is not None and get_id(signal) not in correct:
            show_face(signal)
            first = signal
            state = 1   # clicked
    elif state == 1:    # clicked - clicked once
        if signal is None:
            state = 1   # clicked
        if signal is not None:
            show_face(signal)
            second = signal
            if first != second:
                if get_id(first) == get_id(second):
                    correct.append(get_id(signal))
                    logger.info(f"correct: {correct}")
                    echo(f"Score: {len(correct)}")
                    state = 0   # start
                else:
                    timer.start_wait()
                    state = 2   # wait
                    # fsm()   # TODO: REMOVE WHEN TIMER WORKING
    elif state == 2:    # wait - clicked twice and failed
        if signal is None:
            show_back(first)
            show_back(second)
            # Reinitialize first and second just for info logging.
            first, second = None, None
            state = 0   # start
        if signal is not None:
            state = 2   # clicked
    logger.info(f"    end: {states[state]} {signal} ({first} {second})")

if __name__ == "__main__":
    import time
    timer.fsm = fsm
    timer.run_timer()

    # timeout
    fsm()

    # click same card twice, then correct pair
    fsm((0, 0,))
    fsm((0, 0,))
    fsm((0, 1,))

    # click incorrect pair
    fsm((1, 0,))
    fsm((0, 0,))
    logger.info('sleeping 3s...')
    time.sleep(3)

    # click correct pair
    fsm((1, 0,))
    fsm((1, 1,))

    # click correct pair, again
    fsm((1, 0,))
    fsm((1, 1,))
