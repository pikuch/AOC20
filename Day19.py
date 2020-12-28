# AOC20 day 19
from collections import deque


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


def is_valid(s, rule, rules):
    to_check = deque()
    to_check.append((0, [rule]))  # index, rules to check against
    while len(to_check):
        index, rule_list = to_check.popleft()
        if index == len(s) and len(rule_list) == 0:
            return True
        if index == len(s) or len(rule_list) == 0:
            continue
        if isinstance(rules[rule_list[0]], str):
            if s[index] == rules[rule_list[0]]:
                to_check.append((index + 1, rule_list[1:]))
            else:
                continue
        else:
            for option in rules[rule_list[0]]:
                to_check.append((index, option + rule_list[1:]))
    return False


def run():
    data = load_data("Day19.txt")
    rules, strings = parse_data(data)
    print(sum(is_valid(s, 0, rules) for s in strings))
    # new rules
    magic_limit = 10
    rules[8] = []
    rules[11] = []
    for i in range(1, magic_limit):
        rules[8].append([42] * i)
        rules[11].append([42] * i + [31] * i)
    print(sum(is_valid(s, 0, rules) for s in strings))
