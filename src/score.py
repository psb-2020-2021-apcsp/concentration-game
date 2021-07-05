#!/usr/bin/env python3
#
# score.py
#
import log

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Implement game scoring.
"""
__all__ = ["reset", "score", "matched", "seconds", ]
__author__ = "https://github.com/psb-2020-2021-apcsp/"
__copyright__ = "Copyright 2021, Public Schools of Brookline 2020-2021 APCS-P"
__license__ = "https://choosealicense.com/licenses/mit/"
__version__ = "0.0.1"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Development"

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


if __name__ == "__main__":
    reset()
    right, wrong = 'pyimage47', 'pyimage2'

    # incorrect
    score()

    # correct
    score(right)

    # matched
    for iid in (right, wrong, ):
        logger.info(f"matched('{iid}') = {matched(iid)}")

    # seconds
    numbers = (3,  6,  12,  14,  20,  24,  27,  30,  35,  42,  44,  48,  52, )
    for number in numbers:
        logger.info(f"seconds({number:2d}) = {seconds(number):3d}")
