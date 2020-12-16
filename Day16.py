# AOC20 day 16


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


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
    invalid_list = []
    for ticket in tickets:
        for value in ticket:
            is_valid = False
            for field in field_ranges.values():
                if is_within_field_ranges(value, field):
                    is_valid = True
                    break
            if not is_valid:
                invalid_list.append(value)

    return invalid_list


def run():
    data = load_data("Day16test0.txt")
    field_ranges, my_ticket, other_tickets = parse_data(data)
    print(sum(get_invalid_values(other_tickets, field_ranges)))
