from .Math3D import Point, Vector, Box
from math import floor, sqrt, ceil
epsilon = 0.000001


class Map:
    def __init__(self):
        self.boxes = []

    def max_ray_distance(self) -> int:
        return 50

    def point_to_index(self, point: Point) -> tuple:
        x = int(point.x)
        y = int(point.y)
        return x, y

    # Need this to go in order of boxes closest to o, or it will be incorrect (i think)
    def hit(self, v: Vector, o: Point, theta: float) -> tuple:
        for box in self.boxes:
            intersection = box.intersect(v, o)
            if intersection[0]:
                return (intersection[1], theta)
        return None

    def add_box(self, p: Point) -> None:
        self.boxes.append(Box(p))

    # Right now, accomplishes nothing
    def __str__(self) -> str:
        string = ""
        return string
