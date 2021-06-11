#!/usr/bin/env python3
#
# unittests.py
#
import unittest
import layout
class TestLayoutFunction(unittest.TestCase):

    tests = [
        (2, (2, 1, ), ),
        (32, (8, 4, ), ),
        (106, (53, 2, ), ),
        (64, (8, 8, ), ),
        
    ]
    def test_layouts(self):
        for n, size in self.tests:
            self.assertEqual(layout.sizing(n), size)

unittest.main()
