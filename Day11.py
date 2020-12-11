# AOC20 day 11

def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Seat:
    def __init__(self, occupied):
        self.occupied = occupied
        self.occupied_next = 0
        self.neighbours = []

    def update_occupied(self):
        if self.occupied_next != self.occupied:
            self.occupied = self.occupied_next

    def set_new_occupied(self, crowd):
        if self.occupied == 0 and self.no_neighbours():
            self.occupied_next = 1
            return 1
        elif self.occupied == 1 and self.is_crowded(crowd):
            self.occupied_next = 0
            return 1
        else:
            self.occupied_next = self.occupied
            return 0

    def no_neighbours(self):
        if len(self.neighbours) == 0:
            return True
        for neighbour in self.neighbours:
            if neighbour.occupied:
                return False
        return True

    def is_crowded(self, crowd):
        if len(self.neighbours) < crowd:
            return False
        count = 0
        for neighbour in self.neighbours:
            if neighbour.occupied:
                count += 1
            if count >= crowd:
                return True
        return False


def parse_data_to_close_neighbours(data):
    waiting_room = dict()
    lines = data.split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "L":
                waiting_room[(row, col)] = Seat(0)
    for (row, col), seat in waiting_room.items():
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if (row + dr, col + dc) in waiting_room.keys():
                    seat.neighbours.append(waiting_room[(row + dr, col + dc)])
    return waiting_room


def parse_data_to_visible_neighbours(data):
    waiting_room = dict()
    lines = data.split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "L":
                waiting_room[(row, col)] = Seat(0)
    for (row, col), seat in waiting_room.items():
        for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            steps = 1
            while True:
                if (row + dr * steps) < 0 \
                        or (row + dr * steps) >= len(lines) \
                        or (col + dc * steps) < 0 \
                        or (col + dc * steps) >= len(lines[0]):
                    break
                if (row + dr * steps, col + dc * steps) in waiting_room.keys():
                    seat.neighbours.append(waiting_room[(row + dr * steps, col + dc * steps)])
                    break
                steps += 1
    return waiting_room


def transform_until_stable(waiting_room, crowd):
    changes = 1
    while changes > 0:
        changes = 0
        for seat in waiting_room.values():
            changes += seat.set_new_occupied(crowd)
        for seat in waiting_room.values():
            seat.update_occupied()
        print(f"\rChanges: {changes}", end=" ")
    return sum(map(lambda a: a.occupied, waiting_room.values()))


def run():
    data = load_data("Day11.txt")
    waiting_room_1 = parse_data_to_close_neighbours(data)
    count_1 = transform_until_stable(waiting_room_1, crowd=4)
    print(f"\r When considering closest chairs, {count_1} end up occupied.")
    waiting_room_2 = parse_data_to_visible_neighbours(data)
    count_2 = transform_until_stable(waiting_room_2, crowd=5)
    print(f"\r When considering closest visible chairs, {count_2} end up occupied.")
