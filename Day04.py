# AOC20 day 04


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Passport:
    def __init__(self, init_string):
        self.data = {}
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

        invalidated = False
        for k, v in self.data.items():
            if k == "byr":  # four digits; at least 1920 and at most 2002
                if len(v) != 4:
                    invalidated = True
                if 1920 > int(v) or 2002 < int(v):
                    invalidated = True
            elif k == "iyr":  # four digits; at least 2010 and at most 2020
                if len(v) != 4:
                    invalidated = True
                if 2010 > int(v) or 2020 < int(v):
                    invalidated = True
            elif k == "eyr":  # four digits; at least 2020 and at most 2030
                if len(v) != 4:
                    invalidated = True
                if 2020 > int(v) or 2030 < int(v):
                    invalidated = True
            elif k == "hgt":  # If cm, at least 150 and at most 193 if in, at least 59 and at most 76.
                if v[-2:] == "cm":
                    if 150 > int(v[:-2]) or 193 < int(v[:-2]):
                        invalidated = True
                elif v[-2:] == "in":
                    if 59 > int(v[:-2]) or 76 < int(v[:-2]):
                        invalidated = True
                else:
                    invalidated = True
            elif k == "hcl":  # a # followed by exactly six characters 0-9 or a-f
                if len(v) != 7:
                    invalidated = True
                if v[0] != "#":
                    invalidated = True
                for c in v[1:]:
                    if c not in "0123456789abcdef":
                        invalidated = True
            elif k == "ecl":  # exactly one of: amb blu brn gry grn hzl oth
                if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    invalidated = True
            elif k == "pid":  # a nine-digit number, including leading zeroes
                if len(v) != 9:
                    invalidated = True
                for c in v:
                    if c not in "0123456789":
                        invalidated = True
        if invalidated:
            return False
        return True


def get_passport_list(data):
    return [Passport(line) for line in data.split("\n\n")]


def run():
    data = load_data("Day04.txt")
    passports = get_passport_list(data)
    print(sum(passport.has_all_fields() for passport in passports))  # 219
    print(sum(passport.has_valid_fields() for passport in passports))  # 127

