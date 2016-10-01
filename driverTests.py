import unittest
import sys

class DriveVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        magnitude = (x**2+y**2)**0.5
        other = magnitude * (2-(abs(x)+1))/2
        sys.stdout.write(str(magnitude))
        if x < 0:
            self.lw = magnitude
            self.rw = other
        else:
            self.lw = other
            self.rw = magnitude
class DriveVectorTests(unittest.TestCase):
    def test_x0_y0_left_wheel_0(self):
        vec = DriveVector(0,0)
        self.assertEqual(vec.lw, 0)
    def test_x0_y0_right_wheel_0(self):
        vec = DriveVector(0,0)
        self.assertEqual(vec.rw, 0)
    def test_x_minus_1_y0_left_wheel_1_right_wheel_0(self):
        vec = DriveVector(-1, 0)
        self.assertEqual(vec.rw, 0)
        self.assertEqual(vec.lw, 1)
if __name__ == '__main__':
    unittest.main()
