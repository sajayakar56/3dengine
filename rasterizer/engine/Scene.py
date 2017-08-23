from .Camera import Camera
from .Canvas import Canvas
from .Math3D import Calc as cc
import tkinter as tk

DELTA = 5
DELTA_A = 0.1


class Scene:
    def __init__(self, obj = None):
        self.objects = []
        self.cam = Camera()
        self.canvas = Canvas(tk.Tk(), 800, 800)
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()
        if obj:
            self.objects.append(obj)
        self.draw_scene()
        self.canvas.mainloop()

    def draw_scene(self):
        for obj in self.objects:
            self.canvas.draw_object(obj, self.cam)

    def key(self, event):
        if event.char == "w":
            self.cam.move(*self.cam.forward, DELTA)
        if event.char == "s":
            self.cam.move(*self.cam.backward, DELTA)
        if event.char == "z":
            self.cam.move(0, -DELTA, 0)
        if event.char == "x":
            self.cam.move(0, DELTA, 0)
        # Rotate left
        if event.char == "a":
            self.cam.rotate(0, -DELTA_A, 0)
        if event.char == "d":
            self.cam.rotate(0, DELTA_A, 0)
        if event.char == "q":
            self.cam.rotate(0, 0, DELTA_A)
        if event.char == "e":
            self.cam.rotate(0, 0, -DELTA_A)
        # Create cube
        if event.char == "c":
            f = self.cam.forward
            x, y, z = (self.cam.x + f[0], self.cam.y + f[1], self.cam.z + f[2])
            self.objects.append(cc.create_cube(x, y, z, 1))
        # Fill to wireframe
        if event.char == "n":
            self.canvas.change_fill("")
        # Fill to solid black
        if event.char == "m":
            self.canvas.change_fill("black")
        # Toggle trippy mode
        if event.char == "p":
            self.canvas.trippy = not(self.canvas.trippy)
        self.canvas.clear()
        self.draw_scene()

# A help message
message = """
Controls

WASD: Movement
Z/X: Move up/down
C: Create cube
N: Wireframe
M: Solid
"""
print(message)

        
