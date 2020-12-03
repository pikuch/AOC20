# AOC20 day 03


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def collisions(d_col, d_row, rows):
    row, col = 0, 0
    count = 0
    while row < len(rows):
        if rows[row][col] == "#":
            count += 1
        row += d_row
        col = (col + d_col) % len(rows[0])
    return count


def run():
    data = load_data("Day03.txt").split("\n")
    print(collisions(3, 1, data))
    print(collisions(1, 1, data) * collisions(3, 1, data) * collisions(5, 1, data) * collisions(7, 1, data) * collisions(1, 2, data))
