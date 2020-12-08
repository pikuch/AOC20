# AOC20 day 08
from Handheld import Handheld


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def run():
    data = load_data("Day08.txt").split("\n")
    handheld = Handheld(data)
    print(f"Untouched program result: {handheld.run()}")

    outcome = ""
    for line in range(len(data)):
        if data[line].startswith("nop"):
            data[line] = data[line].replace("nop", "jmp")
            handheld = Handheld(data)
            outcome, value = handheld.run()
            print(f"Modified program result: {outcome} {value}")
            data[line] = data[line].replace("jmp", "nop")
        elif data[line].startswith("jmp"):
            data[line] = data[line].replace("jmp", "nop")
            handheld = Handheld(data)
            outcome, value = handheld.run()
            print(f"Modified program result: {outcome} {value}")
            data[line] = data[line].replace("nop", "jmp")
        else:
            continue
        if outcome == "terminates":
            break
