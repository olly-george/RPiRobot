import unittest
import sys

class DriveVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        magnitude = (x**2+y**2)**0.5
        if magnitude > 1:
            x = x / magnitude
            y = y / magnitude
            magnitude = 1
        other = magnitude * (2-(abs(x)+1))/2
        if y < 0:
            direction = -1
        else:
            direction = 1
        sys.stdout.write("x:" + str(x) + "\n")
        sys.stdout.write("y:" + str(y) + "\n")
        sys.stdout.write("m:" + str(magnitude) + "\n")
        sys.stdout.write("o:" + str(other) + "\n")
        sys.stdout.write("d:" + str(direction) + "\n")

        if x < 0:
            if direction == 1:
                self.rw = magnitude
                self.lw = other
            else:
                sys.stdout.write("expected")
                self.rw = direction * other
                self.lw = direction * magnitude
        else:
            if direction == 1:
                self.rw = other
                self.lw = magnitude
            else:
                self.rw = magnitude * direction
                self.lw = other * direction
class DriveVectorTests(unittest.TestCase):
    def test_stop(self):
        vec = DriveVector(0,0)
        self.assertEqual(vec.lw, 0)
        self.assertEqual(vec.rw, 0)
    def test_rotate_anticlockwise(self):
        vec = DriveVector(-1, 0)
        self.assertEqual(vec.rw, 1)
        self.assertEqual(vec.lw, 0)
    def test_rotate_clockwise(self):
        vec = DriveVector(1,0)
        self.assertEqual(vec.rw, 0)
        self.assertEqual(vec.lw, 1)
    def test_turn_forward_right(self):
        vec = DriveVector(0.7071, 0.7071)
        self.assertAlmostEqual(vec.rw, ((1-0.7071)/2), 4)
        self.assertAlmostEqual(vec.lw, 1, 4)
    def test_rotate_anticlockwise_backwards(self):
        vec = DriveVector(-1, -0.0001);
        self.assertAlmostEqual(vec.rw, 0, 4)
        self.assertAlmostEqual(vec.lw, -1, 4)
    def test_upper_limit_at_1(self):
        vec = DriveVector(0.7071*2, 0.7071*2)
        self.assertAlmostEqual(vec.rw, ((1-0.7071)/2),4)
        self.assertAlmostEqual(vec.lw, 1, 4)
if __name__ == '__main__':
    unittest.main()
