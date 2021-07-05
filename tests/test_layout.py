#!/usr/bin/env python3
#
# test_layout.py
#
import pytest, sys
# Update sys.path to include ../src/.
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '../src')))
import layout

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Unit tests for layout.py.
"""

sizing_tests = [
    (2, (2, 1, ), ),
    (32, (8, 4, ), ),
    (106, (53, 2, ), ),
    (64, (8, 8, ), ),
    (6, (3, 2, ), ),
    (12, (4, 3, ), ),
    (24, (6, 4, ), ),
    (28, (7, 4, ), ),
    (40, (8, 5, ), ),
    (48, (8, 6, ), ),
    (54, (9, 6, ), ),
    (60, (10, 6, ), ),
    (70, (10, 7, ), ),
    (84, (12, 7, ), ),
    (88, (11, 8, ), ),
    (96, (12, 8, ), ),
    (104, (13, 8, ), ),
]
def test_sizing():
    for n, size in sizing_tests:
        assert layout.sizing(n) == size

factor_tests = [
    (8, [1, 2], ),
    (5463458053, [1, ], ),
    (2860486313, [1, ], ),
    (5915587277, [1, ], ),
    (1500450271, [1, ], ),
    (3267000013, [1, ], ),
    (5754853343, [1, ], ),
    (4093082899, [1, ], ),
    (9576890767, [1, ], ),
    (3628273133, [1, ], ),
    (2860486313, [1, ], ),
    (5463458053, [1, ], ),
    (3367900313, [1, ], ),
    (1 * 47293 * 47419 * 47501, [1, 47293, 47419, 47501, ], ),
]
def test_factor():
    for prime, factors in factor_tests:
        assert layout._factor(prime) == factors


if __name__ == "__main__":
    # https://primes.utm.edu/lists/small/small.html
    pass
