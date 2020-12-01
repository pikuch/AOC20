# AOC20 day 01


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def to_numbers(data):
    rows = data.split("\n")
    return list(map(int, rows))


def get_multiplied(numbers):
    seen = set()
    for n in numbers:
        if 2020-n in seen:
            return n*(2020-n)
        else:
            seen.add(n)
    return None


def get_multiplied3(numbers):
    seen = set()
    for n in numbers:
        seen.add(n)
    for x in numbers:
        for y in numbers:
            if 2020-x-y in seen:
                return x*y*(2020-x-y)


def run():
    data = load_data("Day01.txt")
    numbers = to_numbers(data)
    multiplied = get_multiplied(numbers)
    print(multiplied)
    multiplied3 = get_multiplied3(numbers)
    print(multiplied3)
