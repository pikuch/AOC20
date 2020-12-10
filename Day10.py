# AOC20 day 10


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def prepare_list(data):
    joltages = sorted(list(map(int, data.split("\n"))))
    return [0] + joltages + [(joltages[-1] + 3)]


def get_diff_counts(joltages):
    differences = [0]*4
    for i in range(len(joltages)-1):
        print(joltages[i+1] - joltages[i], end=" ")
        differences[joltages[i+1] - joltages[i]] += 1
    return differences


def get_diff_list(joltages):
    diffs = []
    for i in range(len(joltages)-1):
        diffs.append(joltages[i+1] - joltages[i])
    return diffs


def run():
    data = load_data("Day10.txt")
    joltages = prepare_list(data)
    diff_counts = get_diff_counts(joltages)
    print(diff_counts[1] * diff_counts[3])
    #print(get_diff_list())
    print(2**3 * 4**7 * 7**10)

# 3 * [1 1 3] = 2**3
# 7 * [1 1 1 3] = 4**7
# 10 * [1 1 1 1 3] = 7**10
# 37024595836928
