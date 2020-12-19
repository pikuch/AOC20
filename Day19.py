# AOC20 day 19


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Rule:
    def __init__(self, s):
        if s.startswith("\""):
            self.type = "final"
            self.value = s[1]
        else:
            self.type = "options"
            self.value = list(map(lambda option: list(map(int, option.split())), s.split(" | ")))


def get_splits(s, n):
    if n == 1:
        return s
    elif n == 2:
        for num in range(1, len(s)):
            yield s[:num], s[num:]
    else:
        print("Oops!")  # good for now
        exit(1)


class Ruleset:
    def __init__(self, s):
        self.rules = dict()
        for line in s.splitlines():
            rule_number_string, rule_description = line.split(": ")
            self.rules[int(rule_number_string)] = Rule(rule_description)

    def match(self, s, rule):
        if self.rules[rule].type == "final":
            return s == self.rules[rule].value
        else:
            return any(map(lambda subrules: self.match_subrules(s, subrules), self.rules[rule].value))

    def match_subrules(self, s, subrules):
        return any(map(lambda substrings: all(map(lambda sr: self.match(sr[0], sr[1]),
                                                  zip(substrings, subrules))),
                       get_splits(s, len(subrules))))


def parse_data(data):
    rule_data, string_data = data.split("\n\n")
    return Ruleset(rule_data), string_data.splitlines()


def run():
    data = load_data("Day19test0.txt")
    rules, strings = parse_data(data)
    print(sum(map(lambda s: rules.match(s, 0), strings)))
