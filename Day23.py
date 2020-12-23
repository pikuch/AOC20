# AOC20 day 23
from collections import deque


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Cup:
    def __init__(self, value):
        self.val = value
        self.next = self
        self.prev = self


class Cups:
    def __init__(self, data):
        elements = list(map(int, data))
        self.current = last = Cup(elements[0])
        for el in elements[1:]:
            last = self.insert_after(last, Cup(el))
        self.picked = []
        self.destination = self.current

    def insert_after(self, last_cup, new_cup):
        new_cup.next = last_cup.next
        new_cup.prev = last_cup
        new_cup.prev.next = new_cup
        new_cup.next.prev = new_cup
        return new_cup

    def pick_next(self):
        next_cup = self.current.next
        self.current.next = next_cup.next
        next_cup.next.prev = self.current
        return next_cup

    def pick_3(self):
        self.picked.clear()
        for _ in range(3):
            self.picked.append(self.pick_next())

    def place_picked(self):
        cursor = self.destination
        for cup in self.picked:
            cursor = self.insert_after(cursor, cup)

    def is_picked(self, n):
        return self.picked[0].val == n or self.picked[1].val == n or self.picked[2].val == n

    def next_number(self, n):
        return n - 1 if n > 1 else 9

    def cursor_to(self, n):
        while self.current.val != n:
            self.current = self.current.next

    def destination_to(self, n):
        while self.destination.val != n:
            self.destination = self.destination.next

    def go_to_destination(self):
        number = self.next_number(self.current.val)
        while self.is_picked(number):
            number = self.next_number(number)
        self.destination_to(number)

    def move(self):
        #self.show()
        self.pick_3()
        #self.show_picked()
        self.go_to_destination()
        #self.show_destination()
        self.place_picked()
        self.current = self.current.next

    def show(self):
        print(f"({self.current.val})", end="")
        cursor = self.current.next
        while cursor != self.current:
            print(f" {cursor.val} ", end="")
            cursor = cursor.next
        print()

    def show_picked(self):
        for el in self.picked:
            print(f"{el.val} ", end="")
        print()

    def show_destination(self):
        print(self.destination.val)

    def show_after_1(self):
        self.cursor_to(1)
        cursor = self.current.next
        while cursor != self.current:
            print(f"{cursor.val}", end="")
            cursor = cursor.next


def run():
    data = load_data("Day23.txt")
    cups = Cups(data)
    for i in range(100):
        cups.move()
    cups.show_after_1()
