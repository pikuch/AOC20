# AOC20 day 24


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
    x, y, z = 0, 0, 0
    for i in inst:
        x += i[0]
        y += i[1]
        z += i[2]
    if (x, y, z) in tiles:
        tiles.remove((x, y, z))
    else:
        tiles.add((x, y, z))


def count_neighbours(x, y, z, tiles):
    count = 0
    if (x - 2, y + 1, z + 1) in tiles:
        count += 1
    if (x + 2, y - 1, z - 1) in tiles:
        count += 1
    if (x + 1, y - 2, z + 1) in tiles:
        count += 1
    if (x - 1, y + 2, z - 1) in tiles:
        count += 1
    if (x + 1, y + 1, z - 2) in tiles:
        count += 1
    if (x - 1, y - 1, z + 2) in tiles:
        count += 1
    return count


def step(tiles):
    considered = set()
    for x, y, z in tiles:
        considered.add((x, y, z))
        considered.add((x-2, y+1, z+1))
        considered.add((x+2, y-1, z-1))
        considered.add((x+1, y-2, z+1))
        considered.add((x-1, y+2, z-1))
        considered.add((x+1, y+1, z-2))
        considered.add((x-1, y-1, z+2))
    changes = []
    for x, y, z in considered:
        n = count_neighbours(x, y, z, tiles)
        if (x, y, z) in tiles and n not in (1, 2):
            changes.append((x, y, z, 0))
        if (x, y, z) not in tiles and n == 2:
            changes.append((x, y, z, 1))
    # apply changes
    for x, y, z, c in changes:
        if c == 0:
            tiles.remove((x, y, z))
        else:
            tiles.add((x, y, z))


def run():
    data = load_data("Day24.txt")
    instructions = decode(data)
    tiles = set()
    for inst in instructions:
        flip(inst, tiles)
    print(len(tiles))
    for t in range(100):
        print(f"\rstep {t}", end="")
        step(tiles)
    print(f"\nThere are now {len(tiles)} black tiles")
