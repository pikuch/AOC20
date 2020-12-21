# AOC20 day 19


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_data(data):
    rule_data, string_data = data.split("\n\n")
    rules = dict()
    for line in rule_data.splitlines():
        rule_number_string, rule_description = line.split(": ")
        rules[int(rule_number_string)] = parse_rule(rule_description)
    return rules, string_data.splitlines()


def parse_rule(s):
    if s.startswith("\""):
        return s[1]
    else:
        return list(map(lambda option: list(map(int, option.split())), s.split(" | ")))


def consume_several(s, alternative, rules):
    for rule in alternative:
        result, s = consume(s, rule, rules)
        if not result:
            return False, s
    return True, s


def consume(s, rule, rules):
    if isinstance(rules[rule], str):
        if s.startswith(rules[rule]):
            return True, s[len(rules[rule]):]
        else:
            return False, s
    else:  # try consume substrings
        for alternative in rules[rule]:
            result, reminder = consume_several(s, alternative, rules)
            if result:
                return True, reminder
        return False, s


def is_valid(s, rule, rules):
    result, reminder = consume(s, rule, rules)
    return result and not len(reminder)


def run():
    data = load_data("Day19.txt")
    rules, strings = parse_data(data)
    print(sum(is_valid(s, 0, rules) for s in strings))
