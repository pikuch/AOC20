# AOC20 day 23


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


class Cup:
    def __init__(self, value):
        self.val = value
        self.next = self


class Cups:
    def __init__(self, elements):
        self.items = [None] * (len(elements) + 1)  # not using the 0 index
        for element in elements:
            self.items[element] = Cup(element)
        for index in range(len(elements) - 1):
            self.items[elements[index]].next = self.items[elements[index + 1]]
        self.items[elements[len(elements) - 1]].next = self.items[elements[0]]
        self.current = self.items[elements[0]]
        self.destination = self.current
        self.picked = None

    def pick_3(self):
        self.picked = self.current.next
        self.current.next = self.current.next.next.next.next

    def place_picked(self):
        after = self.destination.next
        self.destination.next = self.picked
        self.picked.next.next.next = after

    def is_picked(self, n):
        return self.picked.val == n or self.picked.next.val == n or self.picked.next.next.val == n

    def next_number(self, n):
        return n - 1 if n > 1 else len(self.items) - 1

    def go_to_destination(self):
        number = self.current.val
        while True:
            number = self.next_number(number)
            if not self.is_picked(number):
                break
        self.destination = self.items[number]

    def move(self):
        self.pick_3()
        self.go_to_destination()
        self.place_picked()
        self.current = self.current.next

    def show_after_1(self):
        cursor = self.items[1].next
        while cursor.val != 1:
            print(f"{cursor.val}", end="")
            cursor = cursor.next
        print()


def run():
    data = load_data("Day23.txt")
    cups = Cups(list(map(int, data)))
    for i in range(100):
        cups.move()
    cups.show_after_1()

    cups = Cups(list(map(int, data)) + list(range(len(data)+1, 10**6 + 1)))
    for i in range(10**7):
        cups.move()
        if i % 1000 == 0:
            print(f"\r{100*i/(10**7):.1f}%", end="")
    print(" done")
    first, second = cups.items[1].next.val, cups.items[1].next.next.val
    print(f"{first} * {second} = {first * second}")
