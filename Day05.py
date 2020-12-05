# AOC20 day 05


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_id(code):
    row = int(code[:7], 2)
    col = int(code[7:], 2)
    return row * 8 + col


def id_list(data):
    binary_list = data.translate(str.maketrans("FBLR", "0101")).split("\n")
    return list(map(get_id, binary_list))


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
