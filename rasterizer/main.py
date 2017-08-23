from engine.Scene import Scene
from engine.Math3D import Triangle, Point

obj_file = open("meow.obj", 'r')

line = obj_file.readline()
# Arrays start at 1 xd
vertices = [(0.0, 0.0, 0.0)]
faces = []

while line != "":
    line.strip('\n')
    if line[0] == 'v':
        line = line.split()
        x, y, z = line[1], line[2], line[3]
        vertices.append(Point(float(x), float(y), float(z)))

    if line[0] == 'f':
        line = line.split()[1:]
        line = [int(a.split("/")[0]) for a in line]
        faces.append(line)

    line = obj_file.readline()

triangles = []
# Convert to triangles    
for f in faces:
    if len(f) != 3:
        break
    f = [vertices[a] for a in f]
    triangles.append(Triangle(*f))

s = Scene(triangles)
