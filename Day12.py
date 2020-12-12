# AOC20 day 12
from math import cos, pi, sin, sqrt, atan2


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day12.txt")
    x, y, a = 0, 0, 0
    inst = []
    for line in data.split("\n"):
        inst.append((line[0], int(line[1:])))

    for ii in inst:
        if ii[0] == "N":
            y += ii[1]
        elif ii[0] == "S":
            y -= ii[1]
        elif ii[0] == "E":
            x += ii[1]
        elif ii[0] == "W":
            x -= ii[1]
        elif ii[0] == "L":
            a += ii[1]
        elif ii[0] == "R":
            a -= ii[1]
        elif ii[0] == "F":
            x += ii[1] * cos(a*pi/180)
            y += ii[1] * sin(a*pi/180)

    print(x, y, a, abs(x)+abs(y))

    wx, wy = 10, 1
    x, y, a = 0, 0, 0

    for ii in inst:
        if ii[0] == "N":
            wy += ii[1]
        elif ii[0] == "S":
            wy -= ii[1]
        elif ii[0] == "E":
            wx += ii[1]
        elif ii[0] == "W":
            wx -= ii[1]
        elif ii[0] == "L" or ii[0] == "R":
            da = pi * ii[1] / 180
            radius = sqrt(wx**2 + wy**2)
            if ii[0] == "R":
                da *= -1
            a = atan2(wy, wx) + da
            wx = radius * cos(a)
            wy = radius * sin(a)
        elif ii[0] == "F":
            x += ii[1] * wx
            y += ii[1] * wy

    print(x, y, a, abs(x)+abs(y))
