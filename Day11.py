# AOC20 day 11
import numpy as np


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_data(data):
    lines = data.split("\n")
    seats = np.zeros((len(lines), len(lines[0])), dtype=np.int8)
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == ".":
                seats[row][col] = -1
            else:
                seats[row][col] = 0
    return seats


def count_neighbours(row, col, seats):
    n = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue
            if (row+dr) < 0 or (row+dr) >= seats.shape[0] or (col+dc) < 0 or (col+dc) >= seats.shape[1]:
                continue
            if seats[row+dr][col+dc] == 1:
                n += 1
    return n


def transform(seats):
    changes = 1
    while changes > 0:
        changes = 0
        new_seats = np.empty_like(seats)
        for row in range(seats.shape[0]):
            for col in range(seats.shape[1]):
                neighbours = count_neighbours(row, col, seats)
                if seats[row][col] == 0 and neighbours == 0:
                    new_seats[row][col] = 1
                    changes += 1
                elif seats[row][col] == 1 and neighbours >= 4:
                    new_seats[row][col] = 0
                    changes += 1
                else:
                    new_seats[row][col] = seats[row][col]
        seats = new_seats
        print(changes)
    return seats


def run():
    data = load_data("Day11.txt")
    seats = parse_data(data)
    seats = transform(seats)
    print(seats)
    print(np.sum(seats[seats==1]))
