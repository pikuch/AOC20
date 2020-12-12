# AOC20 day 12

def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def distance_after_naive_rules(instructions):
    x, y, a = 0, 0, 0
    cos_values = {0: 1, 90: 0, 180: -1, 270: 0}
    sin_values = {0: 0, 90: 1, 180: 0, 270: -1}
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
            a = (a + arg + 360) % 360
        elif code == "R":
            a = (a - arg + 360) % 360
        elif code == "F":
            x += arg * cos_values[a]
            y += arg * sin_values[a]
    return abs(x) + abs(y)


def distance_after_actual_rules(instructions):
    x, y = 0, 0
    wx, wy = 10, 1
    cos_values = {0: 1, 90: 0, 180: -1, 270: 0}
    sin_values = {0: 0, 90: 1, 180: 0, 270: -1}
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
            if code == "R":
                arg = (360 - arg) % 360
            wx, wy = cos_values[arg] * wx - sin_values[arg] * wy, sin_values[arg] * wx + cos_values[arg] * wy
        elif code == "F":
            x += arg * wx
            y += arg * wy
    return abs(x) + abs(y)


def run():
    data = load_data("Day12.txt")
    instructions = [(line[0], int(line[1:])) for line in data.split("\n")]
    print(distance_after_naive_rules(instructions))
    print(distance_after_actual_rules(instructions))
