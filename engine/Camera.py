from .Math3D import Calc as c


class Camera:
    def __init__(self, pos, fov, direction, m):
        self.pos, self.fov, self.direction, self.m = pos, fov, direction, m

    # Fix for non integer location of camera
    def cast(self, angle):
        m = self.m
        v = c.angle_to_vector(angle)
        return m.hit(v, self.pos, angle)

    def move(self, v):
        self.pos = c.point_and_vector(self.pos, v)

    def raycast(self, n):
        delta_fov = self.fov / (n - 1)
        theta = self.direction + (self.fov / 2)
        lst = []
        for i in range(n - 1):
            ray = self.cast(theta)
            lst.append(ray)
            theta -= delta_fov
        return lst
