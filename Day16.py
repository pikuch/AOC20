# AOC20 day 16
from functools import reduce


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class TicketField:
    def __init__(self, line):
        self.name, all_ranges = line.split(": ")
        self.ranges = list(map(lambda s: list(map(int, s.split("-"))), all_ranges.split(" or ")))

    def encompasses(self, number):
        return any(map(lambda the_range: the_range[0] <= number <= the_range[1], self.ranges))


class Ticket:
    def __init__(self, line):
        self.numbers = list(map(int, line.split(",")))


def data_to_objects(data):
    blocks = data.split("\n\n")
    fields = list(map(TicketField, blocks[0].splitlines()))
    my_ticket = Ticket(blocks[1].splitlines()[1])
    other_tickets = list(map(Ticket, blocks[2].splitlines()[1:]))
    return fields, my_ticket, other_tickets


def is_valid_number(number, fields):
    return any(map(lambda field: field.encompasses(number), fields))


def get_invalid_numbers(ticket, fields):
    return filter(lambda n: not is_valid_number(n, fields), ticket.numbers)


def is_valid_ticket(ticket, fields):
    return all(map(lambda number: is_valid_number(number, fields), ticket.numbers))


def is_number_valid_for_field(number, field_name, fields):
    return any(map(lambda field: field.name == field_name and field.encompasses(number), fields))


def determine_field_names(valid_tickets, fields):
    options = [set([fields[i].name for i in range(len(fields))]) for j in range(len(fields))]

    for field in range(len(options)):
        for field_name in [fields[i].name for i in range(len(fields))]:
            if not all(map(lambda ticket: is_number_valid_for_field(ticket.numbers[field], field_name, fields), valid_tickets)):
                options[field].discard(field_name)

    field_names = [None] * len(fields)
    found_new = True
    while found_new:
        found_new = False
        for i in range(len(options)):
            if len(options[i]) == 1:
                found_new = True
                field_names[i] = list(options[i])[0]
                for j in range(len(options)):
                    options[j].discard(field_names[i])
                continue

    return field_names


def run():
    data = load_data("Day16.txt")

    fields, my_ticket, other_tickets = data_to_objects(data)
    invalid_number_sum = sum(map(lambda t: sum(get_invalid_numbers(t, fields)), other_tickets))
    valid_tickets = list(filter(lambda t: is_valid_ticket(t, fields), other_tickets))
    print(invalid_number_sum)

    field_names = determine_field_names(valid_tickets, fields)
    departure_pairs = filter(lambda pos: field_names[pos[0]].startswith("departure"), enumerate(my_ticket.numbers))
    print(reduce(lambda x, pos: x * pos[1], departure_pairs, 1))
