#!/usr/bin/env python3
#
# gameplay.py
#
"""
Implement the finite state machine for game play.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

# Initialize module data.
state, states = 0, [ 'start', 'clicked', 'wait', ]
# These are first click position & second click position.
first, second = None, None
# Functions for show_back and show_face... default to print
show_back, show_face = print, print

# TODO: implement game-play FSM
def fsm(signal=None):
    """Perform one step of the game-play FSM by processing signal.
    If signal is a (row, column, ) tuple, then it represents a click
    of that card. If signal is None, then it represents a timeout.
    TODO: a bit of a kludge, but workable for one oddball signal."""
    # Remember state and clicked values.
    global state, first, second
    print(states[state], first, second)
    if state == 0:      # start
        # not yet clicked
        if signal is not None:
            first = signal
            # TODO: show_face for first
            state = 1   # clicked
    elif state == 1:    # clicked
        # clicked once
        if signal is not None:
            # TODO: do stuff here on second click
            pass
    elif state == 2:    # wait
        # clicked twice and failed
        if signal is None:
            # TODO: show_back for first & second
            state = 0   # start
        elif signal != first and signal != second:
            # TODO: what happens if player clicks without waiting?
            pass

if __name__ == "__main__":
    fsm()
