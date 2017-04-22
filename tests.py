from classes import *
origin = Point(0, 0, 0)
m = Map(7, 7, 1)
m[Point(3, 3, 0)] = 1
m[Point(1, 6, 0)] = 1
c = Camera(origin, radians(50), radians(45), m)
