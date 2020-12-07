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


def is_shiny_gold_inside(k, rules):
    for element in rules[k]:
        if element[1] == "shiny gold":
            return True
        if is_shiny_gold_inside(element[1], rules):
            return True
    return False


def count_insides(bag, rules):
    s = 0
    for element in rules[bag]:
        s += element[0] + element[0] * count_insides(element[1], rules)
    return s


def run():
    data = load_data("Day07.txt")
    rules = get_rules(data)
    print(sum(map(lambda k: is_shiny_gold_inside(k, rules), rules.keys())))
    print(count_insides("shiny gold", rules))
