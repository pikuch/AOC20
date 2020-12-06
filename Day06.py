# AOC20 day 06
from collections import defaultdict


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_answers(data):
    answers = []
    current = []
    lines = data.split("\n")
    for line in lines:
        if line == "":
            answers.append(current)
            current = []
        else:
            current.append(line)
    answers.append(current)
    return answers


def run():
    data = load_data("Day06.txt")
    answers = get_answers(data)

    different_counter = 0
    for group in answers:
        different = set()
        for person in group:
            for c in person:
                different.add(c)
        different_counter += len(different)

    print(different_counter)

    same_counter = 0
    for group in answers:
        counts = defaultdict(lambda: 0)
        for person in group:
            for c in person:
                counts[c] += 1
        for ans in counts.values():
            if ans == len(group):
                same_counter += 1

    print(same_counter)
