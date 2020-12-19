# AOC20 day 19
from itertools import combinations


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_rule(s):
    if s.startswith("\""):
        return s[1]
    else:
        return list(map(lambda option: list(map(int, option.split())), s.split(" | ")))


def get_splits(s, n):
    if n == 1:
        return s
    elif n == 2:
        for num in range(1, len(s)):
            yield s[:num], s[num:]
    elif n == 3:
        for i, j in combinations(range(1, len(s)), 2):
            yield s[:i], s[i:j], s[j:]
    else:
        print("Oops!")  # not gonna happen
        exit(1)


class Ruleset:
    def __init__(self, s):
        self.rules = dict()
        for line in s.splitlines():
            rule_number_string, rule_description = line.split(": ")
            self.rules[int(rule_number_string)] = parse_rule(rule_description)

    def match(self, s, rule):
        if isinstance(self.rules[rule], str):
            return s == self.rules[rule]
        else:
            return any(map(lambda subrules: self.match_subrules(s, subrules), self.rules[rule]))

    def match_subrules(self, s, subrules):
        return any(map(lambda substrings: all(map(lambda sr: self.match(sr[0], sr[1]),
                                                  zip(substrings, subrules))),
                       get_splits(s, len(subrules))))


def parse_data(data):
    rule_data, string_data = data.split("\n\n")
    return Ruleset(rule_data), string_data.splitlines()


def run():
    data = load_data("Day19.txt")
    rules, strings = parse_data(data)
    rules.match(strings[0], 0)
    exit(1)
    print(sum([rules.match(s, 0) for s in strings]))
