# AOC20 day 03


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def count_collisions(dc, dr, rows):
    row = 0
    col = 0
    collisions = 0
    while row < len(rows):
        if rows[row][col] == "#":
            collisions += 1
        row += dr
        col = (col + dc) % len(rows[0])
    return collisions


def run():
    data = load_data("Day03.txt")
    rows = data.split("\n")
    collisions = count_collisions(3, 1, rows)
    print(collisions)
    c2 = count_collisions(1, 1, rows) *\
         count_collisions(3, 1, rows) *\
         count_collisions(5, 1, rows) *\
         count_collisions(7, 1, rows) *\
         count_collisions(1, 2, rows)
    print(c2)