# AOC20 day 19


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_data(data):
    rule_data, string_data = data.split("\n\n")
    rules = dict()
    for line in rule_data.splitlines():
        rule_number_string, the_rest = line.split(": ")
        current_rules = the_rest.split(" | ")
        if current_rules[0].startswith("\""):
            rules[int(rule_number_string)] = current_rules[0][1]
        else:
            rule = []
            for r in current_rules:
                rule.append(list(map(int, r.split())))
            rules[int(rule_number_string)] = rule

    return rules, string_data.splitlines()


def get_splits(s, n):
    if n==1:
        return s
    elif n==2:
        for num in range(1, len(s)):
            yield s[:num], s[num:]
    else:
        print("Oops!")  # good for now
        exit(1)


def option_match(s, option, rules):
    return any(map(lambda sss: all(map(lambda sto: msg_match(sto[0], sto[1], rules), zip(sss, option))), get_splits(s, len(option))))


def msg_match(s, rule, rules):
    if isinstance(rules[rule], str):
        return s == rules[rule]
    else:
        matched = False
        for option in rules[rule]:
            if option_match(s, option, rules):
                matched = True
                break
        return matched


def run():
    data = load_data("Day19.txt")
    rules, strings = parse_data(data)

    print(sum(map(lambda s: msg_match(s, 0, rules), strings)))
