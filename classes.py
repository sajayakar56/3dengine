import tkinter as tk
from math import *
from sys import *
import os
from operator import *
default_round = round
epsilon = 0.000001

class Point:
    def __init__(self, *coords):
        self.coords = coords
        self.parent_class = self.__class__
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.z = self.coords[2]

    def floor(self, sector_size):
        lst = []
        for i in self:
            lst.append(i // sector_size)
        return sector_size * Point(*lst)

    def round(self, length):
        lst = []
        for i in self:
            lst.append(round(i, length))
        return self.parent_class(*lst)

    def invert(self):
        return self.parent_class(self.y, self.x, 0)

    def negative(self):
        for i in self:
            if i < 0:
                return True
        return False

    def __repr__(self):
        return "Point{}".format(self.coords)

    def __str__(self):
        return str(self.coords)

    def __add__(self, other):
        return combine_objects(add, self, other)

    def __neg__(self):
        return self.parent_class(*[-i for i in self.coords])

    def __sub__(self, other):
        return self + (-other)

    def __len__(self):
        return len(self.coords)

    def __contains__(self, element):
        return element in self.coords

    def __getitem__(self, index):
        return self.coords[index]

    def __mul__(self, other):
        assert type(other) in (float, int)
        lst = [i * other for i in self]
        return self.parent_class(*lst)

    def __rmul__(self, other):
        return self * other


class Vector(Point):
    def magnitude(self):
        return sqrt(self.dot(self))

    def dot(self, other):
        temp_vector = combine_objects(mul, self, other)
        return sum(temp_vector.coords)

    # Returns y value for given x, consider changing to y_val
    def y(self, x):
        return x * self.y/self.x

    def x(self, y):
        return y * self.x/self.y

    def unit(self):
        return (1 / self.magnitude()) * self

    def abs_max(self):
        return max([abs(i) for i in self])

    def simplify(self, sector_size):
        return (sector_size/self.abs_max()) * self

    def __repr__(self):
        return "Vector{}".format(self.coords)

class Map:
    def __init__(self, length, height, sector_size):
        self.length, self.height, self.sector_size = length, height, sector_size
        self.matrix = []
        for i in range(int(height/sector_size) + 1):
            self.matrix.append([])
            for j in range(int(length/sector_size) + 1):
                self.matrix[i].append(0)

    def max_ray_distance(self):
        return sqrt(self.length**2 + self.height**2)

    def point_to_index(self, point):
        point = (1/self.sector_size) * point

        x, y, z = point
        return (int(x), int(y))

    def step(self, pos, v, inverted=False):
        if v.x > 0:
            dx = floor(pos.x + 1) - pos.x
        else:
            dx = ceil(pos.x - 1) - pos.x
        dy = dx * (v.y / v.x)
        if inverted:
            # return round(Point(pos.y + dy, pos.x + dx, 0), 5)
            return Point(pos.y + dy, pos.x + dx, 0)
        else:
            # return round(Point(pos.x + dx, pos.y + dy, 0), 5)
            return Point(pos.x + dx, pos.y + dy, 0)

    def __getitem__(self, p):
        # Please help
        if hasattr(p.x, "is_integer") and p.x.is_integer():
            test = self.__getitem__(p - Point(epsilon, 0, 0))
            if test:
                return test
        if hasattr(p.y, "is_integer") and p.y.is_integer():
            test = self.__getitem__(p - Point(0, epsilon, 0))
            if test:
                return test
        if p.negative():
            return None
        try:
            p = self.point_to_index(p)
            return self.matrix[p[0]][p[1]]
        except:
            return None

    def __setitem__(self, p1, value):
        p1 = self.point_to_index(p1)
        self.matrix[p1[0]][p1[1]] = value

    # Right now, prints out X and Y swapped
    def __str__(self):
        string = ""
        for i in reversed(range(len(self.matrix))):
            if type(self.sector_size) == int or (i * self.sector_size).is_integer():
                string += str(int(i * self.sector_size)) + " " + str(self.matrix[i]) + "\n"
            else:
                string += "  " + str(self.matrix[i]) + "\n"
        return string

class Canvas(tk.Canvas):
    def __init__(self, root, width, height):
        self.width, self.height = width, height
        self.root = root
        super().__init__(width=self.width, height=self.height)
        self.pack()

    def mainloop(self, camera, faster):
        self.run(camera, faster)
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
        width, delta_width = self.width//n, self.width//n
        lst.append((0, width))
        for i in range(n - 1):
            lst.append((width, width + delta_width))
            width += delta_width
        return lst

    # Faster is how much to decrease # of operations done
    def run(self, camera, faster=1):
        self.clear()
        lst = self.partition(self.width//faster)
        rays = camera.raycast(self.width//faster)
        for i in range(len(rays)):
            if rays[i]:
                ray = rays[i]
                ray = points_to_vector(camera.pos, ray)
                ray_angle = abs(camera.direction - vector_to_angle(ray))
                self.draw_rectangle(lst[i], ((self.height-50)/(ray.magnitude() * cos(ray_angle))))
        self.pack()

class Camera:
    def __init__(self, pos, fov, direction, m):
        self.pos, self.fov, self.direction, self.m = pos, fov, direction, m

    # Fix for non integer location of camera
    def cast(self, angle, r):
        def ray(pos):
            # Base Case 1: Out of Range
            if distance(self.pos, pos) > r:
                return None
            stepX = m.step(pos, v)
            stepY = m.step(pos.invert(), v.invert(), True)
            if distance(pos, stepY) < distance(pos, stepX):
                pos = stepY
            else:
                pos = stepX
            # To prevent the point on vertex problem
            # pos -= Point(epsilon, epsilon, 0)
            # Base Case 2: Found ya!
            if m[pos]:
                return pos
            else:
                return ray(pos)

        m = self.m
        sector_size = m.sector_size
        v = angle_to_vector(angle)
        return ray(self.pos)

    def move(self, v):
        self.pos = point_and_vector(self.pos, v)

    def raycast(self, n):
        delta_fov = self.fov / (n - 1)
        t = self.direction + (self.fov / 2)
        lst = []
        r = self.m.max_ray_distance()
        for i in range(n-1):
            ray = self.cast(t, r)
            lst.append(ray)
            t -= delta_fov
        return lst

def angle_to_vector(x):
    return Vector(cos(x), sin(x), 0)

def distance(p1, p2):
    return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def vector_to_angle(v):
    return atan(v[1]/v[0])

def points_to_vector(p1, p2):
    return Vector(*(p2 - p1).coords)

def point_and_vector(p, v):
    return p + Point(*v.coords)

def frange(n, step_size):
    return [i * step_size for i in range(int(n * 1 / step_size))]

def combine_objects(f, o1, o2):
    assert type(o1) == type(o2), "Adding improper types"
    assert len(o1) == len(o2), "Points are not same dimension"
    lst = []
    for i, j in zip(o1, o2):
        lst.append(f(i, j))
    return o1.parent_class(*lst)

def round(val, length):
    if hasattr(val, "round"):
        return val.round(length)
    return default_round(val, length)
