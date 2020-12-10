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
        differences[joltages[i+1] - joltages[i]] += 1
    return differences


def get_diff_list(joltages):
    diffs = []
    for i in range(len(joltages)-1):
        diffs.append(joltages[i+1] - joltages[i])
    return diffs


def count_paths(diffs):
    segments = []
    index = 0
    segment_length = 0
    while index < len(diffs):
        if diffs[index] == 3:
            segments.append(segment_length)
            segment_length = 0
        elif diffs[index] == 1:
            segment_length += 1
        else:
            return None
        index += 1

    paths = 1
    for segment in segments:  # there are only a few paths through
        if segment == 2:
            paths *= 2
        elif segment == 3:
            paths *= 4
        elif segment == 4:
            paths *= 7

    return paths


def run():
    data = load_data("Day10.txt")
    joltages = prepare_list(data)
    diff_counts = get_diff_counts(joltages)
    print(diff_counts[1] * diff_counts[3])
    print(count_paths(get_diff_list(joltages)))
