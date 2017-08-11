import tkinter as tk
from math import sin, cos, pi
from .Camera import Camera
import threading


class Canvas(tk.Canvas):
    def __init__(self, root, width, height):
        self.width, self.height = width, height
        self.root = root
        super().__init__(width=self.width, height=self.height, bg="white")
        self.pack()

    def mainloop(self):
        self.pack()
        super().mainloop()

    def clear(self):
        self.delete("all")
        self.pack()
        
    # An object is a list of triangles
    def draw_object(self, obj, c: Camera):
        for triangle in obj:
            self.draw_triangle(triangle, c)

    def draw_triangle(self, triangle, c: Camera):
        pixels = []
        cx, cy, cz = c.x, c.y, c.z
        tx, ty, tz = c.tx, c.ty, c.tz
        ex, ey, ez = c.ex, c.ey, c.ez

        for pt in triangle.points:
            ax, ay, az = pt.x, pt.y, pt.z
            x = ax - cx
            y = ay - cy
            z = az - cz

            dx = cos(ty) * (sin(tz) * y + cos(tz) * x) - (sin(ty) * z)
            dy = sin(tx) * (cos(ty) * z + sin(ty) * (sin(tz) * y + cos(tz) * x)) + cos(tx) * (cos(tz) * y - sin(tz) * x)
            dz = cos(tx) * (cos(ty) * z + sin(ty) * (sin(tz) * y + cos(tz) * x)) - sin(tx) * (cos(tz) * y - sin(tz) * x)

            bx = (ez / dz) * dx - ex
            by = (ez / dz) * dy - ey
            pixels.append((bx, by))
        while pixels != []:
            p1 = pixels.pop()
            for p2 in pixels:
                self.create_line(int(p1[0]),
                                 int(p1[1]),
                                 int(p2[0]),
                                 int(p2[1]))
        self.pack()

