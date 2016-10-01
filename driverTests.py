import unittest
import sys

class DriveVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        magnitude = (x**2+y**2)**0.5
        other = magnitude * (2-(abs(x)+1))/2
        if x < 0:
            self.rw = magnitude
            self.lw = other
        else:
            self.rw = other
            self.lw = magnitude
class DriveVectorTests(unittest.TestCase):
    def test_x0_y0_left_wheel_0(self):
        vec = DriveVector(0,0)
        self.assertEqual(vec.lw, 0)
    def test_x0_y0_right_wheel_0(self):
        vec = DriveVector(0,0)
        self.assertEqual(vec.rw, 0)
    def test_x_minus_1_y0_left_wheel_1_right_wheel_0(self):
        vec = DriveVector(-1, 0)
        self.assertEqual(vec.rw, 1)
        self.assertEqual(vec.lw, 0)
    def test_x_1_y_0_left_wheel_0_right_wheel_1(self):
        vec = DriveVector(1,0)
        self.assertEqual(vec.rw, 0)
        self.assertEqual(vec.lw, 1)
    def test_turn_left(self):
        vec = DriveVector(0.7071, 0.7071)
        self.assertAlmostEqual(vec.rw, ((1-0.7071)/2), 4)
        self.assertAlmostEqual(vec.lw, 1, 4)
if __name__ == '__main__':
    unittest.main()
