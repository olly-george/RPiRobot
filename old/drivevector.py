"""Vector that is used to determine wheel speed and robot direction"""
import sys

class drivevector:
    """The vector class"""
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
