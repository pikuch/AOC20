# AOC20 day 14
from collections import deque


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def read_instructions(lines):
    program = []
    for line in lines:
        items = line.split(" = ")
        if items[0] == "mask":
            program.append((items[0], tuple(reversed(items[1]))))
        else:
            program.append([int(items[0][4:-1]), int(items[1])])
    return program


def execute(program, part):
    memory = dict()
    mask = ["X"] * 36
    for inst in program:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            if part == 1:  # part 1: override values with mask
                execute_with_mask(inst, mask, memory)
            else:  # part 2: memory address decoder
                execute_with_mask2(inst, mask, memory)
    return memory


def execute_with_mask(inst, mask, memory):
    value = tuple(reversed(f"{inst[1]:036b}"))
    output = 0
    for bit in range(36):
        if mask[bit] == "X":
            current = value[bit]
        else:
            current = mask[bit]
        output += int(current) * (2 ** bit)
    memory[inst[0]] = output


def execute_with_mask2(inst, mask, memory):
    address = tuple(reversed(f"{inst[0]:036b}"))
    for new_address in generate_addresses(address, mask):
        memory[new_address] = inst[1]


def generate_addresses(address, mask):
    to_check = deque()
    to_check.append((0, 0))
    while len(to_check):
        value, bit = to_check.popleft()
        if bit == 36:
            yield value
        else:
            if mask[bit] == "0":
                to_check.append((value + int(address[bit]) * (2 ** bit), bit + 1))
            elif mask[bit] == "1":
                to_check.append((value + (2 ** bit), bit + 1))
            else:
                to_check.append((value, bit + 1))
                to_check.append((value + (2 ** bit), bit + 1))


def run():  # would be faster to use two 64 bit masks, but python is not the best for that
    data = load_data("Day14.txt")
    program = read_instructions(data.split("\n"))
    memory = execute(program, 1)
    print(sum(memory.values()))
    # assert sum(memory.values()) == 7817357407588
    memory = execute(program, 2)
    print(sum(memory.values()))
    # assert sum(memory.values()) == 4335927555692
