# AOC20 day 12
from math import cos, pi, sin, sqrt, atan2


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def distance_after_naive_rules(instructions):
    x, y, a = 0, 0, 0
    for code, arg in instructions:
        if code == "N":
            y += arg
        elif code == "S":
            y -= arg
        elif code == "E":
            x += arg
        elif code == "W":
            x -= arg
        elif code == "L":
            a += arg
        elif code == "R":
            a -= arg
        elif code == "F":
            x += arg * cos(a*pi/180)
            y += arg * sin(a*pi/180)
    return int(abs(x) + abs(y))


def distance_after_actual_rules(instructions):
    x, y = 0, 0
    wx, wy = 10, 1
    for code, arg in instructions:
        if code == "N":
            wy += arg
        elif code == "S":
            wy -= arg
        elif code == "E":
            wx += arg
        elif code == "W":
            wx -= arg
        elif code == "L" or code == "R":
            da = pi * arg / 180
            if code == "R":
                da *= -1
            r = sqrt(wx ** 2 + wy ** 2)
            a = atan2(wy, wx) + da
            wx = r * cos(a)
            wy = r * sin(a)
        elif code == "F":
            x += arg * wx
            y += arg * wy
    return int(abs(x) + abs(y))


def run():
    data = load_data("Day12.txt")
    instructions = [(line[0], int(line[1:])) for line in data.split("\n")]
    print(distance_after_naive_rules(instructions))  # 2297
    print(distance_after_actual_rules(instructions))  # 89984
