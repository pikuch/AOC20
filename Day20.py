# AOC20 day 20
from math import sqrt
import numpy as np
from collections import deque
from itertools import product


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Puzzle:
    def __init__(self, data):
        self.tiles = [Tile(block) for block in data.split("\n\n")]
        self.grid = dict()
        self.assembly_size = int(sqrt(len(self.tiles))) * (self.tiles[0].pixels.shape[0] - 2)
        self.assembly = np.zeros((self.assembly_size, self.assembly_size), dtype=np.int8)

    def assemble(self):
        self.grid[(0, 0)] = self.tiles.pop()
        to_fill = deque([(-1, 0), (1, 0), (0, -1), (0, 1)])
        while len(to_fill):
            print(f"\r{len(self.grid)} tiles placed", end="")
            row, col = to_fill.pop()
            for tile in self.tiles:
                for rotation in range(8):
                    if self.try_place(tile, row, col):
                        self.grid[(row, col)] = tile
                        self.tiles.remove(tile)
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            neighbour = (row + dr, col + dc)
                            if neighbour not in self.grid.keys() and neighbour not in to_fill:
                                to_fill.append(neighbour)
                        break
                    tile.next_transformation()
        print()
        # put the pixels together
        min_row = min([row for row, col in self.grid.keys()])
        min_col = min([col for row, col in self.grid.keys()])
        for r, c in product(range(self.assembly_size), range(self.assembly_size)):
            self.assembly[r, c] = self.grid[(r // 8 + min_row, c // 8 + min_col)].pixels[1 + (r % 8), 1 + (c % 8)]

        return self.grid[(min_row, min_col)].number * \
               self.grid[(min_row + 11, min_col)].number * \
               self.grid[(min_row, min_col + 11)].number * \
               self.grid[(min_row + 11, min_col + 11)].number

    def try_place(self, tile, row, col):
        if (row - 1, col) in self.grid:
            if np.any(tile.top_edge() != self.grid[(row - 1, col)].bottom_edge()):
                return False
        if (row + 1, col) in self.grid:
            if np.any(tile.bottom_edge() != self.grid[(row + 1, col)].top_edge()):
                return False
        if (row, col - 1) in self.grid:
            if np.any(tile.left_edge() != self.grid[(row, col - 1)].right_edge()):
                return False
        if (row, col + 1) in self.grid:
            if np.any(tile.right_edge() != self.grid[(row, col + 1)].left_edge()):
                return False
        return True

    def check_for_sea_monsters(self):
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        self.assembly = np.flipud(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        self.assembly = np.rot90(self.assembly)
        if self.mark_monsters():
            return np.sum(self.assembly == 1)
        return None

    def mark_monsters(self):
        monster = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
        count = 0
        for row in range(0, self.assembly_size - monster.shape[0] + 1):
            for col in range(0, self.assembly_size - monster.shape[1] + 1):
                if np.all(monster <= self.assembly[row:row + monster.shape[0], col: col + monster.shape[1]]):
                    count += 1
                    self.assembly[row:row + monster.shape[0], col: col + monster.shape[1]] += monster
        return count


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
        self.transformation = 0

    def top_edge(self):
        return self.pixels[0, :]

    def bottom_edge(self):
        return self.pixels[-1, :]

    def left_edge(self):
        return self.pixels[:, 0]

    def right_edge(self):
        return self.pixels[:, -1]

    def next_transformation(self):
        if self.transformation % 4 == 0:
            self.flip()
        self.rotate()
        self.transformation = (self.transformation + 1) % 8

    def rotate(self):
        self.pixels = np.rot90(self.pixels)

    def flip(self):
        self.pixels = np.flipud(self.pixels)


def run():
    data = load_data("Day20.txt")
    puzzle = Puzzle(data)
    print(puzzle.assemble())
    print(puzzle.check_for_sea_monsters())
    # Image.fromarray(puzzle.assembly*120).show()
