from classes import *
import sys
print(sys.argv)
faster = int(sys.argv[1])

# Hardcoded in map
def gen_map(m):
    m[Point(3, 3, 0)] = 1
    m[Point(3, 4, 0)] = 1
    m[Point(1, 6, 0)] = 1
    m[Point(3, 5, 0)] = 1
    m[Point(5, 3, 0)] = 1
    m[Point(5, 4, 0)] = 1
    m[Point(5, 5, 0)] = 1

def key(event):
    if event.char == "q":
        root.destroy()
    if event.char == "w":
        c.move(angle_to_vector(c.direction).unit() * (1/4))
    if event.char == "s":
        c.move(-angle_to_vector(c.direction).unit() * (1/4))
    if event.char == "a":
        c.direction += .1
    if event.char == "d":
        c.direction -= .1
    canvas.run(c, faster)

origin = Point(0, 0, 0)
m = Map(7, 7, 1)
gen_map(m)
c = Camera(origin, radians(70), radians(45), m)
root = tk.Tk()
canvas = Canvas(root, 1600, 900)

bindings = {"w": c.move(angle_to_vector(c.direction).unit()),
            "a": None,
            "s": None,
            "d": c.move(-angle_to_vector(c.direction).unit())}



canvas.bind("<Key>", key)
canvas.focus_set()
canvas.mainloop(c, faster)
