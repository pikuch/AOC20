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
            program.append(items)
        else:
            program.append([int(items[0][4:-1]), int(items[1])])
    return program


def execute_with_mask(inst, mask, memory):
    value = f"{inst[1]:036b}"
    output = 0
    for bit in range(36):
        if mask[-bit-1] == "X":
            output += int(value[-bit-1]) * (2**bit)
        else:
            output += int(mask[-bit-1]) * (2**bit)
    memory[inst[0]] = output


def execute(program):
    memory = dict()
    mask = "X" * 36
    for inst in program:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            execute_with_mask(inst, mask, memory)
    return memory


def generate_addresses(address, mask):
    to_check = deque()
    to_check.append((0, 0))
    while len(to_check):
        value, bit = to_check.popleft()
        if bit == 36:
            yield value
        else:
            if mask[-bit-1] == "0":
                to_check.append((value + int(address[-bit-1]) * (2 ** bit), bit+1))
            elif mask[-bit-1] == "1":
                to_check.append((value + (2 ** bit), bit+1))
            else:
                to_check.append((value, bit + 1))
                to_check.append((value + (2 ** bit), bit + 1))


def execute_with_mask2(inst, mask, memory):
    address = f"{inst[0]:036b}"
    for new_address in generate_addresses(address, mask):
        memory[new_address] = inst[1]


def execute2(program):
    memory = dict()
    mask = "X" * 36
    for inst in program:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            execute_with_mask2(inst, mask, memory)
    return memory


def run():
    data = load_data("Day14.txt")
    program = read_instructions(data.split("\n"))
    memory = execute(program)
    print(sum(memory.values()))
    memory2 = execute2(program)
    print(sum(memory2.values()))
