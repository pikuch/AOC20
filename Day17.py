# AOC20 day 17
from collections import defaultdict


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class ConwayGrid3d:
    def __init__(self, data):
        self.near_tiles = [(dx, dy, dz)
                           for dx in range(-1, 2)
                           for dy in range(-1, 2)
                           for dz in range(-1, 2)
                           if not (dx == dy == dz == 0)]
        self.grid = set()
        lines = data.splitlines()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == "#":
                    self.grid.add((x, y, 0))

    def neighbours(self, x, y, z):
        n = 0
        for dx, dy, dz in self.near_tiles:
            if (x+dx, y+dy, z+dz) in self.grid:
                n += 1
        return n

    def step(self):
        considered = set()
        changed = []
        for x, y, z in self.grid:
            considered.add((x, y, z))
            for dx, dy, dz in self.near_tiles:
                considered.add((x+dx, y+dy, z+dz))
        for x, y, z in considered:
            n = self.neighbours(x, y, z)
            if (x, y, z) not in self.grid and n == 3:
                changed.append((x, y, z, 1))
            elif (x, y, z) in self.grid and (n < 2 or n > 3):
                changed.append((x, y, z, 0))
        for x, y, z, change in changed:
            if change == 1:
                self.grid.add((x, y, z))
            else:
                self.grid.discard((x, y, z))


def load_cubes(lines):
    cubes = defaultdict(lambda: 0)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                cubes[(x, y, 0)] = 1
    return cubes


def neighbours(x, y, z, cubes):
    n = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == dy == dz == 0:
                    continue
                elif cubes[(x+dx, y+dy, z+dz)] == 1:
                    n += 1
    return n


def step(cubes):
    changes = []
    for x in range(-10, 20):
        for y in range(-10, 20):
            for z in range(-7, 8):
                n = neighbours(x, y, z, cubes)
                if cubes[(x, y, z)] == 1 and (n < 2 or n > 3):
                    changes.append((x, y, z, 0))
                if cubes[(x, y, z)] == 0 and n == 3:
                    changes.append((x, y, z, 1))
    for x, y, z, state in changes:
        cubes[(x, y, z)] = state


def load_cubes4(lines):
    cubes = defaultdict(lambda: 0)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                cubes[(x, y, 0, 0)] = 1
    return cubes


def step4(cubes):
    changes = []
    for x in range(-7, 15):
        for y in range(-7, 15):
            for z in range(-7, 8):
                for w in range(-7, 8):
                    n = neighbours4(x, y, z, w, cubes)
                    if cubes[(x, y, z, w)] == 1 and (n < 2 or n > 3):
                        changes.append((x, y, z, w, 0))
                    if cubes[(x, y, z, w)] == 0 and n == 3:
                        changes.append((x, y, z, w, 1))
    for x, y, z, w, state in changes:
        cubes[(x, y, z, w)] = state


def neighbours4(x, y, z, w, cubes):
    n = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx == dy == dz == dw == 0:
                        continue
                    if (x+dx, y+dy, z+dz, w+dw) in cubes.keys():
                        if cubes[(x+dx, y+dy, z+dz, w+dw)] == 1:
                            n += 1
    return n


def run():
    data = load_data("Day17.txt")
    grid = ConwayGrid3d(data)
    for i in range(6):
        grid.step()
    print(len(grid.grid))

    # 240 1180

    exit(1)
    cubes = load_cubes(data.splitlines())
    for i in range(6):
        step(cubes)
    print(sum(cubes.values()))

    cubes4 = load_cubes4(data.splitlines())
    for i in range(6):
        print(i)
        step4(cubes4)
    print(sum(cubes4.values()))
