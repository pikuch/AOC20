# AOC20 day 02


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class PasswordEntry:
    def __init__(self, description):
        items = [item.strip() for item in description.split(" ")]
        self.index1, self.index2 = tuple(map(int, items[0].split("-")))
        self.letter = items[1][0]
        self.password = items[2]

    def is_valid_old(self):
        return self.index1 <= self.password.count(self.letter) <= self.index2

    def is_valid_new(self):
        return (self.password[self.index1 - 1] == self.letter) != (self.password[self.index2 - 1] == self.letter)


def run():
    data = load_data("Day02.txt")
    entries = [PasswordEntry(line) for line in data.split("\n")]
    valid_passwords_old_rules = sum(entry.is_valid_old() for entry in entries)
    print(f"According to the old rules there are {valid_passwords_old_rules} valid passwords")
    valid_passwords_new_rules = sum(entry.is_valid_new() for entry in entries)
    print(f"According to the new rules there are {valid_passwords_new_rules} valid passwords")
