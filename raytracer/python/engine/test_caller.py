import os
import struct


x = os.system("./intersect 0 0 1 1 2 2")
x = x.to_bytes(4, "little")
x = struct.unpack(">f", x)
print(x)
