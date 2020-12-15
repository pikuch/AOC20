# AOC20 day 15


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read

# not space efficient
# def generate(n, numbers):
#     last_seen = dict()
#     for i in range(len(numbers)-1):
#         last_seen[numbers[i]] = i + 1
#
#     while len(numbers) < n:
#         if len(numbers) % 1000 == 0:
#             print(f"\r{len(numbers)}", end="")
#         current = numbers[-1]
#         if current in last_seen.keys():
#             numbers.append(len(numbers) - last_seen[current])
#             last_seen[current] = len(numbers)-1
#         else:
#             last_seen[current] = len(numbers)
#             numbers.append(0)


def get_nth(n, numbers):
    last_seen = dict()
    for i in range(len(numbers) - 1):
        last_seen[numbers[i]] = i + 1
    generated = len(numbers)
    current = numbers[-1]

    while generated < n:
        if generated % 1000 == 0:
            print(f"\r{100*generated/n:.1f}%", end="")
        if current in last_seen.keys():
            new_current = generated - last_seen[current]
            last_seen[current] = generated
            current = new_current
            generated += 1
        else:
            last_seen[current] = generated
            current = 0
            generated += 1
    return current


def run():
    data = load_data("Day15.txt")
    numbers = list(map(int, data.split(",")))
    print(f"\r{get_nth(2020, numbers)}")
    print(f"\r{get_nth(30000000, numbers)}")
