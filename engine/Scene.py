from math import radians
import tkinter as tk
from .Math3D import Point
from .Math3D import Calc as c
from .Map import Map
from .Camera import Camera
from .Canvas import Canvas


class Scene:
    def __init__(self, precision):
        # DEBUG
        # DEBUG_POINT = Point(3, 3, 0)
        # DEBUG_ANGLE = radians(10)
        # END DEBUG
        self.precision = precision
        origin = Point(0, 0, 0)
        self.map = Map()
        self.cam = Camera(origin, radians(70), radians(45), self.map)
        self.canvas = Canvas(tk.Tk(), 1600, 900)
        gen_map(self.map)
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()
        self.canvas.mainloop(self.cam, precision)

    def key(self, event):
        if event.char == "q":
            tk.Tk().destroy()
        if event.char == "w":
            self.cam.move(c.angle_to_vector(self.cam.direction).unit() * (1 / 4))
        if event.char == "s":
            self.cam.move(-c.angle_to_vector(self.cam.direction).unit() * (1 / 4))
        if event.char == "a":
            self.cam.direction += .1
        if event.char == "d":
            self.cam.direction -= .1
        self.canvas.run(self.cam, self.precision)


# Hardcoded in map
# Write a method in Map that lets one easily define a map
def gen_map(m):
    m.add_box(Point(1, 1, 0))
    m.add_box(Point(3, 3, 0))
    m.add_box(Point(3, 4, 0))
    m.add_box(Point(1, 6, 0))
    m.add_box(Point(3, 5, 0))
    m.add_box(Point(5, 3, 0))
    m.add_box(Point(5, 4, 0))
    m.add_box(Point(5, 5, 0))

