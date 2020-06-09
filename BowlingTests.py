import unittest
from BowlingGame import BowlingGame

class BowlingTests(unittest.TestCase):
    def test_roll(self):
        self.assertEqual(0, BowlingGame().roll(0))