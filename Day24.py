# AOC20 day 24
from collections import defaultdict


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def decode(data):
    instructions = []
    for line in data.splitlines():
        dirs = []
        index = 0
        while index < len(line):  # e, se, sw, w, nw, ne
            if line[index] == "e":
                dirs.append((2, -1, -1))
                index += 1
            elif line[index] == "w":
                dirs.append((-2, 1, 1))
                index += 1
            elif line[index] == "s":
                if line[index+1] == "e":
                    dirs.append((1, -2, 1))
                    index += 2
                elif line[index+1] == "w":
                    dirs.append((-1, -1, 2))
                    index += 2
                else:
                    print("Impossible! a parsing error!")
                    exit(1)
            elif line[index] == "n":
                if line[index+1] == "e":
                    dirs.append((1, 1, -2))
                    index += 2
                elif line[index+1] == "w":
                    dirs.append((-1, 2, -1))
                    index += 2
                else:
                    print("Impossible! a parsing error!")
                    exit(1)
        instructions.append(dirs)
    return instructions


def flip(inst, tiles):
    r, c = 0, 0
    for i in inst:
        r += i[0]
        c += i[1]
    tiles[(r, c)] = 1 - tiles[(r, c)]


def run():
    data = load_data("Day24.txt")
    instructions = decode(data)
    tiles = defaultdict(lambda: 0)
    for inst in instructions:
        flip(inst, tiles)
    print(sum(tile == 1 for tile in tiles.values()))
