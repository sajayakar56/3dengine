import tkinter as tk
from .Math3D import Calc as c
from math import cos


class Canvas(tk.Canvas):
    def __init__(self, root, width, height):
        self.width, self.height = width, height
        self.root = root
        super().__init__(width=self.width, height=self.height)
        self.pack()

    def mainloop(self, camera, precision):
        self.run(camera, precision)
        self.pack()
        super().mainloop()

    def clear(self):
        self.delete("all")
        self.pack()

    def draw_rectangle(self, coords, h):
        height = self.height//2
        h = h // 2
        coords = (coords[0], height - h, coords[1], height + h)
        self.create_rectangle(coords, outline="white", fill="black")
        self.pack()

    def partition(self, n):
        lst = []
        width, delta_width = self.width // n, self.width // n
        lst.append((0, width))
        for i in range(n - 1):
            lst.append((width, width + delta_width))
            width += delta_width
        return lst

    # precision is how much to decrease # of operations done
    def run(self, camera, precision=1):
        self.clear()
        lst = self.partition(self.width // precision)
        rays = camera.raycast(self.width // precision)
        for i in range(len(rays)):
            ray = rays[i]
            if ray:
                ray_angle = abs(camera.direction - ray[1])
                ray_dist = ray[0]
                self.draw_rectangle(lst[i], ((self.height - 50) / (ray_dist * cos(ray_angle))))
        self.pack()
