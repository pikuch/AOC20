# AOC20 day 24
from PIL import Image, ImageDraw


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def east(pos):
    return pos[0]+2, pos[1]-1, pos[2]-1


def west(pos):
    return pos[0]-2, pos[1]+1, pos[2]+1


def northeast(pos):
    return pos[0]+1, pos[1]+1, pos[2]-2


def northwest(pos):
    return pos[0]-1, pos[1]+2, pos[2]-1


def southeast(pos):
    return pos[0]+1, pos[1]-2, pos[2]+1


def southwest(pos):
    return pos[0]-1, pos[1]-1, pos[2]+2


class Tiles:
    def __init__(self, data):
        self.tiles = set()
        for line in data.splitlines():
            pos = (0, 0, 0)
            index = 0
            while index < len(line):
                if line[index] == "e":
                    pos = east(pos)
                    index += 1
                elif line[index] == "w":
                    pos = west(pos)
                    index += 1
                elif line[index] == "s":
                    if line[index + 1] == "e":
                        pos = southeast(pos)
                        index += 2
                    elif line[index + 1] == "w":
                        pos = southwest(pos)
                        index += 2
                    else:
                        print("parsing error")
                        exit(1)
                elif line[index] == "n":
                    if line[index + 1] == "e":
                        pos = northeast(pos)
                        index += 2
                    elif line[index + 1] == "w":
                        pos = northwest(pos)
                        index += 2
                    else:
                        print("parsing error")
                        exit(1)
            self.flip(pos)

    def flip(self, pos):
        if pos in self.tiles:
            self.tiles.remove(pos)
        else:
            self.tiles.add(pos)

    def count(self):
        return len(self.tiles)

    def step(self):
        considered = set()
        for pos in self.tiles:
            considered.add(pos)
            considered.add(east(pos))
            considered.add(west(pos))
            considered.add(southeast(pos))
            considered.add(southwest(pos))
            considered.add(northeast(pos))
            considered.add(northwest(pos))
        changes = []
        for pos in considered:
            n = self.count_neighbours(pos)
            if pos in self.tiles and n not in (1, 2):
                changes.append((pos, 0))
            if pos not in self.tiles and n == 2:
                changes.append((pos, 1))
        # apply changes
        for pos, change in changes:
            if change == 1:
                self.tiles.add(pos)
            else:
                self.tiles.remove(pos)

    def count_neighbours(self, pos):
        count = 0
        if east(pos) in self.tiles:
            count += 1
        if west(pos) in self.tiles:
            count += 1
        if southeast(pos) in self.tiles:
            count += 1
        if southwest(pos) in self.tiles:
            count += 1
        if northeast(pos) in self.tiles:
            count += 1
        if northwest(pos) in self.tiles:
            count += 1
        return count


def render(tileset, step):
    WIDTH, HEIGHT = 6000, 6000
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
    ctx = ImageDraw.Draw(img)
    for x, y, z in tileset:
        draw_tile(x, y, z, ctx, WIDTH/2, HEIGHT/2)
    img.save(f".\\imgs\\step{step:03d}.png")


def draw_tile(x, y, z, ctx, cx, cy):
    xx = cx + 15 * x
    yy = cy - 8 * y + 8 * z
    ctx.polygon(((xx+13, yy-7), (xx+13, yy+7), (xx, yy+15), (xx-13, yy+7), (xx-13, yy-7), (xx, yy-15)), (0, 0, 0))


def run():
    data = load_data("Day24.txt")
    tiles = Tiles(data)
    print(tiles.count())
    for t in range(100):
        print(f"\rstep {t}", end="")
        # render(tiles.tiles, t)
        tiles.step()
    print(f"\r{tiles.count()}")
