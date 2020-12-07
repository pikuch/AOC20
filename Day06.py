# AOC20 day 06
from collections import defaultdict


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day06.txt")
    groups = data.split("\n\n")
    different_answers = sum(len(set.union(*map(set, group.split("\n")))) for group in groups)
    same_answers = sum(len(set.intersection(*map(set, group.split("\n")))) for group in groups)
    print(different_answers)
    print(same_answers)
