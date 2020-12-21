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


# def consume_several(s, alternative, rules):
#     for rule in alternative:
#         result, s = consume(s, rule, rules)
#         if not result:
#             return False, s
#     return True, s
#
#
# def consume(s, rule, rules):
#     if isinstance(rules[rule], str):
#         if s.startswith(rules[rule]):
#             return True, s[len(rules[rule]):]
#         else:
#             return False, s
#     else:  # try consume substrings
#         for alternative in rules[rule]:
#             if alternative[0] == rule:  # a loop!
#                 for i in range(10, 0, -1):  # consume greadily
#                     result, reminder = consume_several(s, alternative[1:] * i, rules)
#                     if result:
#                         return True, reminder
#             else:
#                 result, reminder = consume_several(s, alternative, rules)
#                 if result:
#                     return True, reminder
#         return False, s
#
#
# def is_valid(s, rule, rules):
#     result, reminder = consume(s, rule, rules):
#     if result and not len(reminder):
#         return True
#     return False


# def consume_several(s, alternative, rules):
#     for rule in alternative:
#         for result in consume(s, rule, rules):
#             if result is None:
#                 yield None
#     yield result
#
#
# def consume(s, rule, rules):
#     if isinstance(rules[rule], str):
#         if s.startswith(rules[rule]):
#             yield s[len(rules[rule]):]
#         else:
#             yield None
#     else:  # try consume substrings
#         for alternative in rules[rule]:
#             if alternative[0] == rule:  # a loop!
#                 for i in range(10, 0, -1):  # consume greadily
#                     for result in consume_several(s, alternative[1:] * i, rules):
#                         if result is not None:
#                             yield result
#             else:
#                 for result in consume_several(s, alternative, rules):
#                     if result is not None:
#                         yield result
#         yield None
#
# def is_valid(s, rule, rules):
#     return any([result == "" for result in consume(s, rule, rules)])


def is_valid(s, rule, rules):
    to_check = deque()
    to_check.append((s, rule, tuple()))
    while len(to_check):
        s, rule, leftovers = to_check.popleft()
        if isinstance(rules[rule], str):
            if s.startswith(rules[rule]):
                if len(leftovers) > 0:
                    to_check.append(s[len(rules[rule]):], )
                yield
            else:
                yield None
        else:  # try consume substrings



def run():
    data = load_data("Day19test0.txt")
    rules, strings = parse_data(data)
    print(sum(is_valid(s, 0, rules) for s in strings))
    for s in strings:
        print(s, is_valid(s, 0, rules))
    exit(1)
    # new rules
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    print(sum(is_valid(s, 0, rules) for s in strings))
