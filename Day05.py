# AOC20 day 05


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def calculate_id(code):
    return int(code, 2)


def id_list(data):
    binary_list = data.translate(str.maketrans("FBLR", "0101")).split("\n")
    return list(map(calculate_id, binary_list))


def get_missing(ids):
    ids.sort()
    for i in range(len(ids)-1):
        if ids[i + 1] != ids[i] + 1:
            return ids[i] + 1


def run():
    data = load_data("Day05.txt")
    ids = id_list(data)
    print(max(ids))
    print(get_missing(ids))
