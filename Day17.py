# AOC20 day 17


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


class ConwayGrid4d:
    def __init__(self, data):
        self.near_tiles = [(dx, dy, dz, dw)
                           for dx in range(-1, 2)
                           for dy in range(-1, 2)
                           for dz in range(-1, 2)
                           for dw in range(-1, 2)
                           if not (dx == dy == dz == dw == 0)]
        self.grid = set()
        lines = data.splitlines()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == "#":
                    self.grid.add((x, y, 0, 0))

    def neighbours(self, x, y, z, w):
        n = 0
        for dx, dy, dz, dw in self.near_tiles:
            if (x+dx, y+dy, z+dz, w+dw) in self.grid:
                n += 1
        return n

    def step(self):
        considered = set()
        changed = []
        for x, y, z, w in self.grid:
            considered.add((x, y, z, w))
            for dx, dy, dz, dw in self.near_tiles:
                considered.add((x+dx, y+dy, z+dz, w+dw))
        for x, y, z, w in considered:
            n = self.neighbours(x, y, z, w)
            if (x, y, z, w) not in self.grid and n == 3:
                changed.append((x, y, z, w, 1))
            elif (x, y, z, w) in self.grid and (n < 2 or n > 3):
                changed.append((x, y, z, w, 0))
        for x, y, z, w, change in changed:
            if change == 1:
                self.grid.add((x, y, z, w))
            else:
                self.grid.discard((x, y, z, w))


def run():
    data = load_data("Day17.txt")
    grid = ConwayGrid3d(data)
    for i in range(6):
        grid.step()
    print(len(grid.grid))

    grid = ConwayGrid4d(data)
    for i in range(6):
        grid.step()
    print(len(grid.grid))
