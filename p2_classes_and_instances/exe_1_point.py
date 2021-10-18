import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)


p = Point(2, 4)
p.set_x(3)
p.set_y(8)
print(p.distance(10, 2))

