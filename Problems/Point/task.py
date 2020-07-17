import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
