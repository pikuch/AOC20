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
    subject_number = public_key
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


def run():
    data = load_data("Day25test0.txt")
    card_public_key, door_public_key = list(map(int, data.splitlines()))
    card_loop_size = calculate_loop_size(card_public_key)
    door_loop_size = calculate_loop_size(door_public_key)
    door_private_key = calculate_encryption_key(card_public_key, door_loop_size)
    card_private_key = calculate_encryption_key(door_public_key, card_loop_size)
    print(f"Card public key: {card_public_key}, card loop size: {card_loop_size}, card private key: {card_private_key}")
    print(f"Door public key: {door_public_key}, door loop size: {door_loop_size}, door private key: {door_private_key}")
