import sys
from engine.Scene import Scene

def main(precision: int):
    s = Scene(precision)

if __name__ == "__main__":
    print(sys.argv)
    precision = int(sys.argv[1])
    main(precision)
