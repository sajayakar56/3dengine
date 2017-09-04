import tkinter as tk
from math import sin, cos, pi
from .Camera import Camera
import random


class Canvas(tk.Canvas):
    def __init__(self, root, width, height):
        self.width, self.height = width, height
        self.root = root
        self.fill = ""
        self.trippy = False
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
        # Shoutout to Wikipedia's fast triangle transform algorithm <3
        cx, cy, cz = c.x, c.y, c.z
        tx, ty, tz = c.tx, c.ty, c.tz
        ex, ey, ez = -self.width // 2, -self.height // 2, 400

        for pt in triangle.points:
            ax, ay, az = pt
            x = ax - cx
            y = ay - cy
            z = az - cz

            dx = cos(ty) * (sin(tz) * y + cos(tz) * x) - (sin(ty) * z)
            dy = sin(tx) * (cos(ty) * z + sin(ty) * (sin(tz) * y + cos(tz) * x)) + cos(tx) * (cos(tz) * y - sin(tz) * x)
            dz = cos(tx) * (cos(ty) * z + sin(ty) * (sin(tz) * y + cos(tz) * x)) - sin(tx) * (cos(tz) * y - sin(tz) * x)

            if dz < 0:
                return None

            bx = (ez / dz) * dx - ex
            by = (ez / dz) * dy - ey
            pixels.append((bx, by))
        self.draw_relative_triangle(pixels)
        self.pack()

    # Can add a fill pass?
    def draw_relative_triangle(self, pixels) -> None:
        if self.trippy:
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            color = "#%02x%02x%02x" % (r, g, b)
            self.create_polygon(pixels, fill=color)
            return
        self.create_polygon(pixels, fill=self.fill, outline='black')

    def change_fill(self, new: str) -> None:
        self.fill = new

    def valid_pixel(self, px: tuple) -> bool:
        return (px[0] > 0) and (px[1] > 0)

