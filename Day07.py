# AOC20 day 07


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_rules(data):
    rules = dict()
    data = data.replace("bags", "").replace("bag", "").replace(".", "")
    for line in data.split("\n"):
        bag, contents = line.split("contain")
        if contents.strip() == "no other":
            rules[bag.strip()] = []
        else:
            inner_list = list(map(str.strip, contents.split(",")))
            counts_list = []
            for elem in inner_list:
                count, name1, name2 = elem.split()
                counts_list.append([int(count), name1 + " " + name2])
            rules[bag.strip()] = counts_list
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
    rules = parse_rules(data)
    print(sum(map(lambda bag: is_shiny_gold_inside(bag, rules), rules.keys())))
    print(count_insides("shiny gold", rules))
