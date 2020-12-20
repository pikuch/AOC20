# AOC20 day 19
from itertools import combinations
from functools import lru_cache


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
        yield [s]
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

    @lru_cache()
    def match(self, s, rule):
        if isinstance(self.rules[rule], str):
            return s == self.rules[rule]
        else:
            for subrules in self.rules[rule]:
                if self.match_subrules(s, tuple(subrules)):
                    return True
            return False

    @lru_cache()
    def match_subrules(self, s, subrules):
        for subs in get_splits(s, len(subrules)):
            all_match = True
            for i in range(len(subrules)):
                if not self.match(subs[i], subrules[i]):
                    all_match = False
                    break
            if all_match:
                return True
        return False


def parse_data(data):
    rule_data, string_data = data.split("\n\n")
    return Ruleset(rule_data), string_data.splitlines()


def run():
    data = load_data("Day19.txt")

    # TODO: parse into a state machine and step from state to state in O(n)

    rules, strings = parse_data(data)
    for s in strings[:1]:
        print(rules.match(strings[0], 0))
#    exit(0)
    print(sum([rules.match(s, 0) for s in strings]))
