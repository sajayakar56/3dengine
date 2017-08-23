import sys
from engine.Scene import Scene

def main(precision: int):
    s = Scene(precision)

if __name__ == "__main__":
    precision = int(sys.argv[1])
    message = """
    Controls\n
    WASD: Movement
    Q: Quit
    1: Decrease FoV 
    2: Increase FoV
    3: Lower precision
    4: Increase precision"""
    print(message)
    main(precision)
