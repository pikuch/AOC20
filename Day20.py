# AOC20 day 20


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Tile:
    def __init__(self, data):
        lines = data.splitlines()
        self.number = int(lines[0][5:9])
        self.pixels = lines[1:]
        self.edges = []
        self.edges.append(list(self.pixels[0]))
        self.edges.append(list(reversed(self.pixels[0])))
        self.edges.append(list(self.pixels[9]))
        self.edges.append(list(reversed(self.pixels[9])))
        left = []
        for row in range(10):
            left.append(self.pixels[row][0])
        self.edges.append(left)
        self.edges.append(list(reversed(left)))
        right = []
        for row in range(10):
            right.append(self.pixels[row][9])
        self.edges.append(right)
        self.edges.append(list(reversed(right)))


def fits_only_two(tile, tiles):
    lone_edges = 0
    for edge in tile.edges:
        match = 0
        for t in tiles:
            if t == tile:
                continue
            for matched in t.edges:
                if edge == matched:
                    match += 1
                    break
        if match == 0:
            lone_edges += 1
    return lone_edges > 2


def run():
    data = load_data("Day20.txt")
    tiles = list(map(Tile, data.split("\n\n")))
    for tile in tiles:
        if fits_only_two(tile, tiles):
            print(tile.number, " * ", end="")

