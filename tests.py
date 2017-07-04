import sys
from math import radians
from engine.Map import Map
from engine.Canvas import Canvas
from engine.Camera import Camera
from engine.Math3D import Vector, Point


origin = Point(0, 0, 0)
m = Map()
camera = Camera(origin, radians(70), radians(45), m)
# Placing one block at (1, 1, 0)
m.add_box(Point(1, 1, 0))

print(m.hit(Vector(1, 1, 0), origin, radians(45)))
print(m.hit(Vector(-1, -1, 0), origin, radians(45)))
