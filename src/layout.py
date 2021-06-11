#!/usr/bin/env python3
#
# layout.py
#
import math
"""
Functions to calulate card layout.
"""
1234567890123456789012345678901234567890123456789012345678901234567890
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
    return result

def factor(n):
    """Return list of factors of n <= sqrt(n)."""
    return [ i for i in range(1, int(math.sqrt(n) + 1))
        if n % i == 0 ]
"""
# Test even numbers on [2, 106]
for i in range(2, 106 + 1, 2):
    w, h = sizing(i)
    # width wihin 3 of height
    if w - h <= 3:
        print(f"{i} {sizing(i)};", end=' ')
"""