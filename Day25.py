# AOC20 day 25


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def calculate_loop_size(public_key):
    subject_number = 7
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value = (value * subject_number) % 20201227
    return loop_size


def calculate_encryption_key(public_key, loop_size):
    subject_number = 7
    value = public_key
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


def run():
    data = load_data("Day25test0.txt")
    card_public_key, door_public_key = list(map(int, data.splitlines()))
    card_loop_size = calculate_loop_size(card_public_key)
    door_loop_size = calculate_loop_size(door_public_key)
    print(calculate_encryption_key(card_public_key, door_loop_size))
    print(calculate_encryption_key(door_public_key, card_loop_size))
