# AOC20 day 04


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def count_valid(data):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    fields_ok = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = 0
    lines = data.split("\n\n")
    for line in lines:
        elements = line.split()
        present_fields = []
        for elem in elements:
            field, value = elem.split(":")
            present_fields.append(field)
        for f in fields_ok:
            if f not in present_fields:
                break
        else:
            valid += 1
    return valid


def count_valid2(data):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    fields_ok = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = 0
    lines = data.split("\n\n")
    for line in lines:
        elements = line.split()
        present_fields = []
        invalidated = False
        for elem in elements:
            field, value = elem.split(":")
            if field == "byr":  # four digits; at least 1920 and at most 2002
                if len(value) != 4:
                    invalidated = True
                if 1920 > int(value) or 2002 < int(value):
                    invalidated = True
            elif field == "iyr":  # four digits; at least 2010 and at most 2020
                if len(value) != 4:
                    invalidated = True
                if 2010 > int(value) or 2020 < int(value):
                    invalidated = True
            elif field == "eyr":  # four digits; at least 2020 and at most 2030
                if len(value) != 4:
                    invalidated = True
                if 2020 > int(value) or 2030 < int(value):
                    invalidated = True
            elif field == "hgt":  # If cm, at least 150 and at most 193 if in, at least 59 and at most 76.
                if value[-2:] == "cm":
                    if 150 > int(value[:-2]) or 193 < int(value[:-2]):
                        invalidated = True
                elif value[-2:] == "in":
                    if 59 > int(value[:-2]) or 76 < int(value[:-2]):
                        invalidated = True
                else:
                    invalidated = True
            elif field == "hcl":  # a # followed by exactly six characters 0-9 or a-f
                if len(value) != 7:
                    invalidated = True
                if value[0] != "#":
                    invalidated = True
                for c in value[1:]:
                    if c not in "0123456789abcdef":
                        invalidated = True
            elif field == "ecl":  # exactly one of: amb blu brn gry grn hzl oth
                if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    invalidated = True
            elif field == "pid":  # a nine-digit number, including leading zeroes
                if len(value) != 9:
                    invalidated = True
                for c in value:
                    if c not in "0123456789":
                        invalidated = True

            present_fields.append(field)
        for f in fields_ok:
            if f not in present_fields:
                break
        else:
            if not invalidated:
                valid += 1
    return valid


def run():
    data = load_data("Day04.txt")
    print(count_valid(data))  # 219
    print(count_valid2(data))  # 127

