from math import pi, cos, sin


class Camera:
    def __init__(self):
        # Coordinates of camera
        self.x, self.y, self.z = (0, 0, -1)
        # Angle
        self.tx, self.ty, self.tz = (0, 0, 0)

    def move(self, x, y, z, s = 1.0):
        self.x += x * s
        self.y += y * s
        self.z += z * s

    def rotate(self, x, y, z):
        self.tx += x
        self.ty += y
        self.tz += z

    @property
    def forward(self) -> tuple:
        tx, ty, tz = self.tx, self.ty, self.tz
        return (cos(tx) * sin(ty), sin(tx) * cos(ty), cos(ty))

    @property
    def backward(self) -> tuple:
        f = self.forward
        return (-f[0], -f[1], -f[2])

    # This is definitely wrong
    @property
    def right(self) -> tuple:
        f = self.forward
        return (f[2], f[1], f[0])
