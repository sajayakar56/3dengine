from .Camera import Camera
from .Canvas import Canvas
from .Math3D import Calc as cc
import tkinter as tk


class Scene:
    def __init__(self):
        self.objects = []
        self.cam = Camera()
        self.canvas = Canvas(tk.Tk(), 800, 800)
        self.objects.append(cc.create_cube(1, 1, 0, 1))
        self.objects.append(cc.create_cube(2, 1, 0, 1))
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()
        self.draw_scene()
        self.canvas.mainloop()

    def draw_scene(self):
        for obj in self.objects:
            self.canvas.draw_object(obj, self.cam)

    def key(self, event):
        if event.char == "a":
            self.cam.move(-1, 0, 0)
        if event.char == "d":
            self.cam.move(1, 0, 0)
        if event.char == "w":
            self.cam.move(0, 0, 1)
        if event.char == "s":
            self.cam.move(0, 0, -1)
        # Rotate left
        if event.char == "q":
            self.cam.rotate(0, -0.1, 0)
        if event.char == "e":
            self.cam.rotate(0, 0.1, 0)
        self.canvas.clear()
        self.draw_scene()
