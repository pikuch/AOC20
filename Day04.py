# AOC20 day 04
import re


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Passport:
    def __init__(self, init_string):
        self.data = {}
        self.rules = {"byr": re.compile(r"^(19[2-8][0-9]|199[0-9]|200[0-2])$"),
                      "iyr": re.compile(r"^(201[0-9]|2020)$"),
                      "eyr": re.compile(r"^(202[0-9]|2030)$"),
                      "hgt": re.compile(r"^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$"),
                      "hcl": re.compile(r"^#[0-9a-f]{6}$"),
                      "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
                      "pid": re.compile(r"^\d{9}$"),
                      "cid": re.compile(r".*")}
        fields = init_string.split()
        for field in fields:
            k, v = field.split(":")
            self.data[k] = v

    def has_all_fields(self):
        needed_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for field in needed_fields:
            if field not in self.data.keys():
                return False
        return True

    def has_valid_fields(self):
        if not self.has_all_fields():
            return False
        for k, v in self.data.items():
            if not self.rules[k].match(v):
                return False
        return True


def get_passport_list(data):
    return [Passport(line) for line in data.split("\n\n")]


def run():
    data = load_data("Day04.txt")
    passports = get_passport_list(data)
    print(sum(passport.has_all_fields() for passport in passports))  # 219
    print(sum(passport.has_valid_fields() for passport in passports))  # 127

