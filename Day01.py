# AOC20 day 01
from itertools import product


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def make_set_and_list(data):
    rows = data.split("\n")
    numbers = list(map(int, rows))
    return set(numbers), numbers


def find_two_parts_of_2020(number_set, number_list):
    for n in number_list:
        if 2020-n in number_set:
            return n, 2020-n
    return None


def find_three_parts_of_2020(number_set, number_list):
    for m, n in product(number_list, number_list):
        if 2020 - m - n in number_set:
            return m, n, 2020 - m - n
    return None


def run():
    data = load_data("Day01.txt")
    number_set, number_list = make_set_and_list(data)
    a, b = find_two_parts_of_2020(number_set, number_list)
    print(f"The two numbers that add up to 2020 are {a} and {b} and their product is {a * b}")
    # 542619
    i, j, k = find_three_parts_of_2020(number_set, number_list)
    print(f"The three numbers that add up to 2020 are {i}, {j} and {k} and their product is {i * j * k}")
    # 32858450
