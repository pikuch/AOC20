# AOC20 day 13
from math import gcd


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_data(data):
    lines = data.split("\n")
    arrival = int(lines[0])
    busses = []
    for element in lines[1].split(","):
        if element != "x":
            busses.append(int(element))
    return arrival, busses


def calculate_answer_1(arrival, busses):
    wait_times = [bus - arrival % bus for bus in busses]
    return list(wait * bus for wait, bus in zip(wait_times, busses) if wait == min(wait_times))[0]


def parse_times(data):
    lines = data.split("\n")
    times = []
    shift = 0
    for element in lines[1].split(","):
        if element != "x":
            times.append((int(element), shift))
        shift += 1
    return times


def calculate_timestamp(times):  # See Chinese Remainder Theorem
    t = times[0][1]
    period = times[0][0]
    for i in range(1, len(times)):
        while (t + times[i][1]) % times[i][0] != 0:
            t += period
        period *= times[i][0]
    return t


def run():
    data = load_data("Day13.txt")
    arrival, busses = parse_data(data)
    print(calculate_answer_1(arrival, busses))

    times = parse_times(data)
    print(calculate_timestamp(times))
