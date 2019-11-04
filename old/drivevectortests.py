"""Tests for the driving vector"""
import unittest
from drivevector import *
class drivevectortests(unittest.TestCase):
    def test_stop(self):
        vec = drivevector(0,0)
        self.assertEqual(vec.lw, 0)
        self.assertEqual(vec.rw, 0)
    def test_rotate_anticlockwise(self):
        vec = drivevector(-1, 0)
        self.assertEqual(vec.rw, 1)
        self.assertEqual(vec.lw, 0)
    def test_rotate_clockwise(self):
        vec = drivevector(1,0)
        self.assertEqual(vec.rw, 0)
        self.assertEqual(vec.lw, 1)
    def test_turn_forward_right(self):
        vec = drivevector(0.7071, 0.7071)
        self.assertAlmostEqual(vec.rw, ((1-0.7071)/2), 4)
        self.assertAlmostEqual(vec.lw, 1, 4)
    def test_rotate_anticlockwise_backwards(self):
        vec = drivevector(-1, -0.0001);
        self.assertAlmostEqual(vec.rw, 0, 4)
        self.assertAlmostEqual(vec.lw, -1, 4)
    def test_upper_limit_at_1(self):
        vec = drivevector(0.7071*2, 0.7071*2)
        self.assertAlmostEqual(vec.rw, ((1-0.7071)/2),4)
        self.assertAlmostEqual(vec.lw, 1, 4)
if __name__ == '__main__':
    unittest.main()
