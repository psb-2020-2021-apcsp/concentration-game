#!/usr/bin/env python3
#
# score.py
#
import log

"""
Implement game scoring.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

logger = log.log(__name__)  # initialize logger

# Initialize module data.
correct, incorrect = list(), 0
# Callback for echo w/ default.
echo = logger.info

def reset():
    global correct, incorrect
    correct, incorrect = list(), 0

def score(cid=None):
    """Score cid in correct list if not None, otherwise increment incorrect."""
    global correct, incorrect
    if cid:
        correct += [cid, ]
    else:
        incorrect += 1
    logger.info(f"(+{len(correct)}, -{incorrect}) {correct}")
    echo(f"Score: {len(correct)} right, {incorrect} wrong")

def matched(cid):
    """Return True if pos in correct, otherwise False."""
    return cid in correct

def seconds(pairs):
    """Return countdown time (in seconds) for pairs matches."""
    return pairs * 4
