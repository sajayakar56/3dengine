import sys
from math import radians
from engine.Map import Map
from engine.Canvas import Canvas
from engine.Camera import Camera
from engine.Math3D import Vector, Point


ORIGIN = Point(0, 0, 0)
TEST_POINT = Point(2.181224380692791, -0.4811199800800545, 0)
TEST_ANGLE = 1.6853981633974489

m = Map()
camera = Camera(TEST_POINT, radians(70), TEST_ANGLE, m)
# Placing one block at (1, 1, 0)
m.add_box(Point(1, 1, 0))
m.add_box(Point(2, 1, 0))
return_val = camera.raycast(10)

print("Tests finished")
