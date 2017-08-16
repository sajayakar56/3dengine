from .Camera import Camera
from .Canvas import Canvas
from .Math3D import Calc as cc
import tkinter as tk

DELTA = 1
DELTA_A = 0.1


class Scene:
    def __init__(self):
        self.objects = []
        self.cam = Camera()
        self.canvas = Canvas(tk.Tk(), 800, 800)
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()
        self.objects.append(custom_object)
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
        self.canvas.clear()
        print(self.cam.x, self.cam.y, self.cam.z)
        self.draw_scene()
		
custom_object = cc.create_object(4.368765, 5.815874, -0.095789,
5.574538, 6.349047, -0.993057,
4.928927, 6.404949, -1.104831,
4.096089, 4.717202, -1.434874,
3.826323, 5.201405, -0.712651,
4.017453, 5.388590, -2.088802,
4.702402, 6.113257, -2.331049,
4.824013, 6.803198, -1.078962,
3.688710, 5.479269, -2.319638,
3.415190, 5.269945, -0.539744,
6.218577, 4.988560, -2.640173,
6.646803, 5.393147, -0.987019,
5.769952, 4.544945, 0.356418,
5.037382, 3.604362, -0.409845,
4.350905, 3.913157, -1.317388,
5.124627, 3.677646, -1.054345,
6.031322, 4.016579, -1.356916,
5.144541, 4.251518, -2.258740,
4.966305, 4.814800, -2.677487,
5.224259, 5.909474, -2.632200,
4.175981, 3.751546, -0.113640,
4.792171, 5.506553, 0.277258,
4.114200, 6.062461, 0.236877,
3.748840, 6.375395, -1.279657,
4.535188, 6.433119, -2.642769)
