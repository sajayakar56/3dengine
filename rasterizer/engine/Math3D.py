from math import sqrt, sin, cos, atan, floor
from operator import add, mul


# 3D Primitive, collection of three points
# Consider storing some extra data to help with fill shading?
class Triangle:
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.points = [p1, p2, p3]

    @property
    def p1(self):
        return self.points[0]

    @property
    def p2(self):
        return self.points[1]

    @property
    def p3(self):
        return self.points[2]

    def __str__(self):
        return "Triangle: " + str(self.p1) + str(self.p2) + str(self.p3)

    def __repr__(self):
        return self.__str__()

        
class Calc:
    # Creates a series of faces with a pass in stream of vertices
    def create_object(*args):
        nums = []
        points = []
        triangles = []
        for a in args:
            nums.append(a)
            if len(nums) == 3:
                points.append(Point(*nums))
                nums = []
            if len(points) == 3:
                triangles.append(Triangle(*points))
                points = []
        return triangles

    # Creates cube from bottom left point
    def create_cube(x, y, z, l: int = 1) -> list:
        return Calc.create_object(x, y, z,
                                  x + l, y, z,
                                  x, y + l, z,

                                  x + l, y, z,
                                  x + l, y + l, z,
                                  x, y + l, z,

                                  x, y, z + l,
                                  x + l, y, z + 1,
                                  x, y + l, z + 1,

                                  x + l, y, z + l,
                                  x + l, y + l, z + l,
                                  x, y + l, z + l,

                                  x, y, z,
                                  x + l, y, z,
                                  x, y, z + l,

                                  x, y, z + l,
                                  x + 1, y, z + l,
                                  x + l, y, z,

                                  x, y, z,
                                  x, y + l, z,
                                  x, y + l, z + l,

                                  x, y + l, z + l,
                                  x, y, z + l,
                                  x, y, z,

                                  x + l, y + l, z,
                                  x, y + l, z,
                                  x, y + l, z + l,

                                  x, y + l, z + l,
                                  x + l, y + l, z + l,
                                  x + l, y + l, z,

                                  x + l, y + l, z,
                                  x + l, y, z,
                                  x + l, y, z + l,

                                  x + l, y, z + l,
                                  x + l, y + l, z + l,
                                  x + l, y + l, z)
