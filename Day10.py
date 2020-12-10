# AOC20 day 10


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_diff(joltages):
    differences = [0]*4
    for i in range(len(joltages)-1):
        differences[joltages[i+1] - joltages[i]] += 1
    return differences


def run():
    data = load_data("Day10.txt").split("\n")
    joltages = sorted(list(map(int, data)))
    joltages = [0] + joltages + [(joltages[-1] + 3)]
    differences = get_diff(joltages)
    print(differences[1]*differences[3])

