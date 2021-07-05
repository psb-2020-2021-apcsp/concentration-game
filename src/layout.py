#!/usr/bin/env python3
#
# layout.py
#
import log, math

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Functions to calulate card layout.
"""
__all__ = ["sizing", ]
__author__ = "https://github.com/psb-2020-2021-apcsp/"
__copyright__ = "Copyright 2021, Public Schools of Brookline 2020-2021 APCS-P"
__license__ = "https://choosealicense.com/licenses/mit/"
__version__ = "0.0.1"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Development"

logger = log.log(__name__)  # initialize logger


def sizing(n):
    """Return a tuple (width, height) where width * height = n and
    absolute value of difference is minimal."""
    assert n > 0, f"{n} <= 0"
    assert n % 2 == 0, f"{n} is not even"
    factors, result = _factor(n), (n, 1, )
    for f in factors:
        trial = (n // f, f, )
        if abs(trial[0] - trial[1]) < abs(result[0] - result[1]):
            result = trial
    logger.debug(f"{n} {result}")
    return result


def _factor(n):
    """Return list of factors of n <= sqrt(n)."""
    return [i for i in range(1, int(math.sqrt(n) + 1)) if n % i == 0]


if __name__ == "__main__":
    pairs = tuple()
    # Test even numbers on [2, 106].
    for i in range(2, 106 + 1, 2):
        w, h = sizing(i)
        # Print ratio 1 +/- 15%.
        if abs(((w * 691) / (h * 1056)) - 1) <= 0.15:
            logger.info(f"{i} {(w, h, )} {(w * 691) / (h * 1056):.2f}")
            pairs += (i // 2, )
    logger.info(f"_numbers in app: {pairs}")
