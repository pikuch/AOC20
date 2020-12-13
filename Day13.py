# AOC20 day 13


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


def run():
    data = load_data("Day13test0.txt")
    arrival, busses = parse_data(data)

    wait_times = [bus - arrival % bus for bus in busses]
    print(list(wait*bus for wait, bus in zip(wait_times, busses) if wait == min(wait_times)))


