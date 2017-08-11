from math import sin, cos, radians, pi

ax, ay, az = (5, 1, -1)
cx, cy, cz = (0, 0, 1)
tx, ty, tz = (pi, pi, 0)
ex, ey, ez = (0, 0, 1)
x = ax - cx
y = ay - cy
z = az - cz

# Check the following statements
dx = cos(ty) * (sin(tz) * y + cos(tz) * x) - (sin(ty) * z)
dy = sin(tx) * (cos(ty) * z + sin(ty) * (sin(tz) * y + cos(tz) * x)) + cos(tx) * (cos(tz) * y - sin(tz) * x)
dz = cos(tx) * (cos(ty) * z + sin(ty) * (sin(tz) * y + cos(tz) * x)) - sin(tx) * (cos(tz) * y - sin(tz) * x)

bx = (ez / dz) * dx - ex
by = (ez / dz) * dy - ey
print(bx, by)
