# AOC20 day 20
import numpy as np
from itertools import product
from PIL import Image, ImageDraw


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Puzzle:
    def __init__(self, data):
        self.tiles = [Tile(block) for block in data.split("\n\n")]
        self.grid = dict()
        self.spaces = set()

    def assemble(self):
        self.grid[(0, 0)] = self.tiles.pop()
        self.spaces.update(((-1, 0), (1, 0), (0, -1), (0, 1)))
        new_added = 1
        while new_added:
            new_added = 0
            for tile, pos in product(self.tiles, self.spaces):
                if self.try_add(tile, pos):
                    new_added += 1
                    break
            print(f"\rassembled {len(self.grid)} pieces", end="")

    def try_add(self, tile, pos):
        for _ in range(4):
            if self.fits(tile, pos):
                self.grid[pos] = tile
                self.tiles.remove(tile)
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (pos[0]+dr, pos[1]+dc) not in self.grid:
                        self.spaces.add((pos[0]+dr, pos[1]+dc))
                self.spaces.discard(pos)
                return True
            tile.rotate()
        tile.flip()
        for _ in range(4):
            if self.fits(tile, pos):
                self.grid[pos] = tile
                self.tiles.remove(tile)
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (pos[0]+dr, pos[1]+dc) not in self.grid:
                        self.spaces.add((pos[0]+dr, pos[1]+dc))
                self.spaces.discard(pos)
                return True
            tile.rotate()

    def fits(self, tile, pos):
        if (pos[0]-1, pos[1]) in self.grid:
            if np.any(self.grid[(pos[0]-1, pos[1])].pixels[-1][:] != tile.pixels[0][:]):
                return False
        if (pos[0]+1, pos[1]) in self.grid:
            if np.any(self.grid[(pos[0]+1, pos[1])].pixels[0][:] != tile.pixels[-1][:]):
                return False
        if (pos[0], pos[1]-1) in self.grid:
            if np.any(self.grid[(pos[0], pos[1]-1)].pixels[:][-1] != tile.pixels[:][0]):
                return False
        if (pos[0], pos[1]+1) in self.grid:
            if np.any(self.grid[(pos[0], pos[1]+1)].pixels[:][0] != tile.pixels[:][-1]):
                return False
        return True


class Tile:
    def __init__(self, data):
        lines = data.splitlines()
        self.number = int(lines[0][5:9])
        lines = lines[1:]
        self.pixels = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
        for row in range(len(lines)):
            for col in range(len(lines[0])):
                if lines[row][col] == "#":
                    self.pixels[row][col] = 1

    def rotate(self, times=1):
        self.pixels = np.rot90(self.pixels, times)

    def flip(self):
        self.pixels = np.flipud(self.pixels)


def run():
    data = load_data("Day20.txt")
    puzzle = Puzzle(data)

    puzzle.assemble()

    row_set = set()
    col_set = set()
    for row, col in puzzle.grid.keys():
        row_set.add(row)
        col_set.add(col)

    img = Image.new("RGB", (1400, 1400))
    ctx = ImageDraw.Draw(img)

    for row, col in puzzle.grid.keys():
        r = row - min(row_set)
        c = col - min(col_set)
        for y, x in product(range(10), range(10)):
            if puzzle.grid[(row, col)].pixels[y][x] == 1:
                ctx.rectangle((c * 103 + x*10, r * 103 + y*10, c * 103 + x*10+9, r * 103 + y*10+9),
                              (240, 240, 200))

    img.show()
