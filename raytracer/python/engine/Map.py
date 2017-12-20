from .Math3D import Point, Vector, Box
from math import floor, sqrt, ceil
epsilon = 0.000001


class Map:
    def __init__(self):
        self.boxes = []
        # Dictionary from tuple(coords) -> list of indexes of boxes

    def max_ray_distance(self) -> int:
        return 50

    def point_to_index(self, point: Point) -> tuple:
        x = int(point.x)
        y = int(point.y)
        return x, y

    # Need this to go in order of boxes closest to o, or it will be incorrect (i think)
    def hit(self, v: Vector, o: Point, theta: float) -> tuple:
        intersections = []
        for box in self.boxes:
            intersection = box.intersect(v, o)
            if intersection[0]:
                intersections.append(intersection)
        if intersections:
            return_val = min(intersections, key=lambda x: x[1])
            return (return_val[1], theta)
        return None

    def add_box(self, p: Point) -> None:
        self.boxes.append(Box(p))

    # Right now, accomplishes nothing
    def __str__(self) -> str:
        string = ""
        return string
