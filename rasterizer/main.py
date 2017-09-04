from engine.Scene import Scene
from engine.Math3D import Triangle


# def error_handler(s: str, data: str = "") -> None:
#     print(s)
#     print(data)
#     input()
#     quit()

obj_file = open("meow.obj", 'r')

line = obj_file.readline()
# Arrays start at 1 xd
vertices = [(0.0, 0.0, 0.0)]
faces = []

# Consider rewriting this with a switch
while line != "":
    line.strip('\n')
    # Vertex case
    if line[0:2] == 'v ':
        line = line.split()
        x, y, z = line[1], line[2], line[3]
        vertices.append((float(x), float(y), float(z),))

    # Face case
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

