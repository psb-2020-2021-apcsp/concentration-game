#!/usr/bin/env python3
#
# unittests.py
#
import layout, unittest, pytest

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Unittests for concentration game functions.
"""


class TestLayoutFunction(unittest.TestCase):

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
    def test_sizing(self):
        for n, size in self.sizing_tests:
            self.assertEqual(layout.sizing(n), size)
            assert layout.sizing(n) == size
 
    factor_tests = [
        (8, [1,2], ),
        (5463458053, [1,], ),
        (2860486313, [1,], ),
        (5915587277, [1,], ),
        (1500450271, [1,], ),
        (3267000013, [1,], ),
        (5754853343, [1,], ),
        (4093082899, [1,], ),
        (9576890767, [1,], ),
        (3628273133, [1,], ),
        (2860486313, [1,], ),
        (5463458053, [1,], ),
        (3367900313, [1,], ),
    ]
    def test_factor(self):
        for prime, factors in self.factor_tests:
            self.assertEqual(layout.factor(prime), factors)
            assert layout.factor(prime) == factors

if __name__ == "__main__":
    # https://primes.utm.edu/lists/small/small.html
    unittest.main()
