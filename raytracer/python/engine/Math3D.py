from math import sqrt, sin, cos, atan, floor
from operator import add, mul            


# Interface for Point and Vector
class Super2D:
    def __init__(self, *coords):
        self.coords = (coords[0], coords[1], 0)
        self.parent_class = self.__class__

    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def z(self):
        return self.coords[2]

    def __str__(self):
        return str(self.coords)

    def __add__(self, other):
        return Calc.combine_objects(add, self, other)

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
        new_coords = (other * self.x, other * self.y, 0)
        return self.parent_class(*new_coords)

    def __rmul__(self, other):
        return self * other
    
    # Floors to integer values
    def floor(self):
        return self.parent_class(list(map(floor(self.coords))))

    def round(self, length):
        return self.parent_class(list(map(round(self.coords, length))))

    def invert(self):
        return self.parent_class(self.y, self.x, 0)
        
    def negative(self):
        return any(n < 0 for n in self.coords)
        

class Point(Super2D):
    # Euclidean distance for xy
    def distTo(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def __repr__(self):
        return "Point{}".format(self.coords)


class Vector(Super2D):
    def magnitude(self):
        return sqrt(self.dot(self))

    def dot(self, other):
        temp_vector = Calc.combine_objects(mul, self, other)
        return sum(temp_vector.coords)

    def unit(self):
        return (1 / self.magnitude()) * self

    def abs_max(self):
        return max([abs(i) for i in self])

    def simplify(self, sector_size):
        return (sector_size / self.abs_max()) * self

    def __repr__(self):
        return "Vector{}".format(self.coords)


class Box:
    def __init__(self, p: Point):
        self.x = int(p.x)
        self.y = int(p.y)
        self.point = Point(self.x + 0.5, self.y + 0.5, 0)

    # From tavianator.com, fast vector AABB
    def intersect(self, v: Vector, o: Point) -> tuple:
        tmin = -100000
        tmax = 100000
        if (v.x != 0):
            tx1 = (self.x - o.x) / v.x
            tx2 = (self.x + 1 - o.x) / v.x

            tmin = max(tmin, min(tx1, tx2))
            tmax = min(tmax, max(tx1, tx2))
        
        if (v.y != 0):
            ty1 = (self.y - o.y) / v.y
            ty2 = (self.y + 1 - o.y) / v.y

            tmin = max(tmin, min(ty1, ty2))
            tmax = min(tmax, max(ty1, ty2))

        if tmax >= 0:
            x = o.x + (tmin * v.x)
            y = o.y + (tmin * v.y)

            dist = sqrt((o.x - x) ** 2 + (o.y - y) ** 2)
            return (tmax >= tmin, dist)
        return (None, None,)


class Calc:
    def angle_to_vector(x):
        return Vector(cos(x), sin(x), 0)

    def vector_to_angle(v):
        return atan(v.y / v.x)

    def points_to_vector(p1, p2):
        return Vector(p2.x - p1.x, p2.y - p1.y, 0)

    def point_and_vector(p, v):
        return Point(p.x + v.x, p.y + v.y, 0)

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
        return round(val, length)

if __name__ == "__main__":
    b = Box(Point(1, 1, 0))
    o = Point(0.0, 0.0, 0)
    v = Vector(0, 0.5, 0)

    print(b.intersect(v, o))
