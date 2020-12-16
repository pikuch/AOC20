# AOC20 day 16


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


##### old, ugly code below

def parse_data(data):
    blocks = data.split("\n\n")
    field_lines = blocks[0].splitlines()
    my_ticket_lines = blocks[1].splitlines()
    other_tickets_lines = blocks[2].splitlines()

    field_ranges = dict()
    for line in field_lines:
        field_name, ranges = line.split(": ")
        range_strings = ranges.split(" or ")
        range_list = []
        for r in range_strings:
            range_list.append(list(map(int, r.split("-"))))
        field_ranges[field_name] = range_list

    my_ticket = list(map(int, my_ticket_lines[1].split(",")))

    other_tickets = []
    for line in other_tickets_lines[1:]:
        other_tickets.append(list(map(int, line.split(","))))

    return field_ranges, my_ticket, other_tickets


def is_within_field_ranges(value, field):
    within = False
    for field_range in field:
        if field_range[0] <= value <= field_range[1]:
            within = True
            break
    return within


def get_invalid_values(tickets, field_ranges):
    invalid_value_list = []
    valid_tickets = []
    for ticket in tickets:
        is_ticket_valid = True
        for value in ticket:
            is_valid = False
            for field in field_ranges.values():
                if is_within_field_ranges(value, field):
                    is_valid = True
                    break
            if not is_valid:
                invalid_value_list.append(value)
                is_ticket_valid = False
        if is_ticket_valid:
            valid_tickets.append(ticket)

    return invalid_value_list, valid_tickets


def does_not_fit(val, field):
    fits = False
    for field_range in field:
        if field_range[0] <= val <= field_range[1]:
            fits = True
            break
    return not fits


def determine_fields(tickets, field_ranges):
    field_options = [set(field_ranges.keys()) for i in tickets[0]]
    determined = [""] * len(tickets[0])
    undetermined_counter = len(tickets[0])

    for i in range(len(determined)):
        for k in field_ranges.keys():
            can_be = True
            for j in range(len(tickets)):
                # field i, ticket j, field_range k
                if does_not_fit(tickets[j][i], field_ranges[k]):
                    can_be = False
                    break
            if not can_be:
                field_options[i].discard(k)

    while undetermined_counter > 0:
        for i in range(len(determined)):
            if len(field_options[i]) == 1:
                determined[i] = list(field_options[i])[0]
                undetermined_counter -= 1
                for j in range(len(determined)):
                    field_options[j].discard(determined[i])
                break
    return determined


def run():
    data = load_data("Day16.txt")
    field_ranges, my_ticket, other_tickets = parse_data(data)
    invalid_values, valid_tickets = get_invalid_values(other_tickets, field_ranges)
    print(sum(invalid_values))

    field_names = determine_fields(valid_tickets, field_ranges)
    det = 1
    for i in range(len(field_names)):
        if field_names[i].startswith("departure"):
            det *= my_ticket[i]
    print(det)

    fields, my_ticket, other_tickets = data_to_objects(data)
    invalid_number_sum = sum(map(lambda t: sum(get_invalid_numbers(t, fields)), other_tickets))
    valid_tickets = list(filter(lambda t: is_valid_ticket(t, fields), other_tickets))
    print(invalid_number_sum)