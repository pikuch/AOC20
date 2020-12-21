# AOC20 day 19
from itertools import combinations
from functools import lru_cache


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_data(data):
    rule_data, string_data = data.split("\n\n")
    return StateMachine(rule_data), string_data.splitlines()


def parse_rule(s):
    if s.startswith("\""):
        return s[1]
    else:
        return list(map(lambda option: list(map(int, option.split())), s.split(" | ")))


class State:
    def __init__(self, value, options):
        self.value = value
        self.options = options


class StateMachine:
    def __init__(self, data):
        self.rules = dict()
        for line in data.splitlines():
            rule_number_string, rule_description = line.split(": ")
            self.rules[int(rule_number_string)] = parse_rule(rule_description)

        finish = State("finish", [])
        start = State("start", [])
        start.options = self.evaluate_states(0, finish)
        self.states = start

    def evaluate_states(self, rule, downstream):
        if isinstance(self.rules[rule], str):
            return State(self.rules[rule], [downstream])
        else:
            options = []
            for alternative in self.rules[rule]:
                link = downstream
                for new_rule in reversed(alternative):
                    node = State(self.evaluate_states(new_rule, link), link)
                    link = node
                options.append(node)
            return [State("", options)]


# class Ruleset:
#     def __init__(self, s):
#         self.rules = dict()
#         for line in s.splitlines():
#             rule_number_string, rule_description = line.split(": ")
#             self.rules[int(rule_number_string)] = parse_rule(rule_description)
#
#     @lru_cache()
#     def match(self, s, rule):
#         if isinstance(self.rules[rule], str):
#             return s == self.rules[rule]
#         else:
#             for subrules in self.rules[rule]:
#                 if self.match_subrules(s, tuple(subrules)):
#                     return True
#             return False
#
#     @lru_cache()
#     def match_subrules(self, s, subrules):
#         for subs in get_splits(s, len(subrules)):
#             all_match = True
#             for i in range(len(subrules)):
#                 if not self.match(subs[i], subrules[i]):
#                     all_match = False
#                     break
#             if all_match:
#                 return True
#         return False


def run():
    data = load_data("Day19test0.txt")
    state_machine, strings = parse_data(data)
    print(state_machine.states)

    # TODO: parse into a state machine and step from state to state in O(n)

    # print(sum([rules.match(s, 0) for s in strings]))
