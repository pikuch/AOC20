# AOC20 day 02
from collections import namedtuple
from functools import reduce


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_entries(data):
    lines = data.split("\n")
    entry = namedtuple("Entry", ["low", "high", "letter", "password"])
    entries = []
    for line in lines:
        rule, password = line.split(":")
        low_high, letter = rule.split()
        low, high = map(int, low_high.split("-"))
        entries.append(entry(int(low), int(high), letter, password.strip()))
    return entries


def is_valid_password(entry):
    return entry.low <= entry.password.count(entry.letter) <= entry.high


def count_valid_passwords(entries):
    counter = 0
    for entry in entries:
        if is_valid_password(entry):
            counter += 1
    return counter


def is_valid_password2(entry):
    return (entry.password[entry.low-1] == entry.letter) + (entry.password[entry.high-1] == entry.letter) == 1


def count_valid_passwords2(entries):
    counter = 0
    for entry in entries:
        if is_valid_password2(entry):
            counter += 1
    return counter


def run():
    data = load_data("Day02.txt")
    entries = parse_entries(data)
    print(count_valid_passwords(entries))  # 548
    print(count_valid_passwords2(entries))
