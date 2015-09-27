"""
There seems to be some glitch in the online editor not allowing to import math.
"""

from unittest import TestCase
import random
from math import sqrt


def is_square(n):
    if n > 1:
        return True if sqrt(n).is_integer() else False
    return False


class TestSquare(TestCase):
    def test(self):
        self.assertTrue(is_square(25))
        self.assertTrue(is_square(16))
        self.assertTrue(is_square(9))
        self.assertTrue(is_square(4))
        self.assertTrue(is_square(36))
        self.assertTrue(is_square(81))
        self.assertTrue(is_square(100))
        self.assertTrue(is_square(9801))
        self.assertFalse(is_square(24))
        self.assertFalse(is_square(99))
        self.assertFalse(is_square(-1))
        self.assertFalse(is_square(0))

    def test_random(self):
        for i in range(1,100):
            r = random.randint(0, 0xfff0)
            self.assertTrue(is_square(r * r))