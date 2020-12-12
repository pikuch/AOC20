# AOC20 day 12
from math import cos, pi, sin


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day12test0.txt")
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
        elif ii[0] == "L":
            wx1 = wx*cos(ii[1]*pi/180) - wy*sin(ii[1]*pi/180)
            wy1 = wx*sin(ii[1]*pi/180) + wy*cos(ii[1]*pi/180)
            wx, wy = wx1, wy1
        elif ii[0] == "R":
            wx1 = -wx*cos(ii[1]*pi/180) + wy*sin(ii[1]*pi/180)
            wy1 = -wx*sin(ii[1]*pi/180) - wy*cos(ii[1]*pi/180)
            wx, wy = wx1, wy1
        elif ii[0] == "F":
            x += ii[1] * wx
            y += ii[1] * wy

    print(x, y, a, abs(x)+abs(y))
