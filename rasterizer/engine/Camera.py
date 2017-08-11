from math import pi


class Camera:
    def __init__(self):
        # Coordinates of camera
        self.x, self.y, self.z = (0, 0, -1)
        # Angle
        self.tx, self.ty, self.tz = (0, 0, 0)
        # Distance from the plane (figure this shit out lol)
        self.ex, self.ey, self.ez = (0, 0, 100)

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def rotate(self, x, y, z):
        self.tx += x
        self.ty += y
        self.tz += z
