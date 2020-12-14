# AOC20 day 14


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


def run():
    data = load_data("Day14.txt")
    program = read_instructions(data.split("\n"))
    memory = execute(program)
    print(sum(memory.values()))
