# AOC20 day 09
from itertools import combinations


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def is_invalid(value, preceding):
    for m, n in combinations(preceding, 2):
        if m + n == value:
            return False
    return True


def find_invalid(signal, preamble):
    for index in range(preamble, len(signal)):
        if is_invalid(signal[index], signal[index-preamble : index]):
            return signal[index]
    return None


def find_series_limits(signal, key):
    for start in range(len(signal)):
        s = 0
        s_list = []
        length = 0
        while s < key:
            s += signal[start+length]
            s_list.append(signal[start+length])
            length += 1
        if s == key:
            return sorted(s_list)
    return None


def run():
    data = load_data("Day09.txt")
    signal = list(map(int, data.split("\n")))
    key = find_invalid(signal, 25)
    print(key)
    series = find_series_limits(signal, key)
    print(min(series) + max(series))
