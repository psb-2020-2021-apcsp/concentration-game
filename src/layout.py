#!/usr/bin/env python3
#
# layout.py
#
import math
import log

"""
Functions to calulate card layout.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

logger = log.log(__name__)  # initialize logger

def sizing(n):
    """Return a tuple (width, height) where width * height = n and
    absolute value of difference is minimal."""
    assert n > 0, f"{n} <= 0"
    assert n % 2 == 0, f"{n} is not even"
    factors, result = factor(n), (n, 1, )
    for f in factors:
        trial = (n // f, f, )
        if abs(trial[0] - trial[1]) < abs(result[0] - result[1]):
            result = trial
    logger.debug(f"{n} {result}")
    return result

def factor(n):
    """Return list of factors of n <= sqrt(n)."""
    return [ i for i in range(1, int(math.sqrt(n) + 1))
        if n % i == 0 ]

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
