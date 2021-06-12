#!/usr/bin/env python3
#
# unittests.py
#
import layout, unittest

"""
Unittests for concentration game functions.
"""
1234567890123456789012345678901234567890123456789012345678901234567890

class TestLayoutFunction(unittest.TestCase):

    sizing_tests = [
        (2, (2, 1, ), ),
        (32, (8, 4, ), ),
        (106, (53, 2, ), ),
        (64, (8, 8, ), ),
    ]
    def test_sizing(self):
        for n, size in self.sizing_tests:
            self.assertEqual(layout.sizing(n), size)

    # TODO: add factor test

if __name__ == "__main__":
    # https://primes.utm.edu/lists/small/small.html
    primes = [
        5915587277,
        1500450271,
        3267000013,
        5754853343,
        4093082899,
        9576890767,
        3628273133,
        2860486313,
        5463458053,
        3367900313,
    ]
    print([layout.factor(n) for n in primes])
    unittest.main()
