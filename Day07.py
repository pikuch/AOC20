# AOC20 day 07


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_rules(data):
    rules = dict()
    for line in data.split("\n"):
        outer, inner = line.split("contain")
        outer = outer.replace("bags", "").strip()
        inner = inner.replace("bags", "")
        inner = inner.replace("bag", "")
        inner = inner.replace(".", "")
        inner = inner.replace("no other", "").strip()
        inner_list = list(map(str.strip, inner.split(",")))
        contents = []
        if inner_list[0] != "":
            for elem in inner_list:
                count, name1, name2 = elem.split()
                contents.append([int(count), name1 + " " + name2])
        rules[outer] = contents
    return rules


def is_shiny_gold_inside(bag, rules):
    for contents in rules[bag]:
        if contents[1] == "shiny gold" or is_shiny_gold_inside(contents[1], rules):
            return True
    return False


def count_insides(bag, rules):
    return sum((element[0] * (1 + count_insides(element[1], rules)) for element in rules[bag]))


def run():
    data = load_data("Day07.txt")
    rules = get_rules(data)
    print(sum(map(lambda bag: is_shiny_gold_inside(bag, rules), rules.keys())))
    print(count_insides("shiny gold", rules))
