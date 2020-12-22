# AOC20 day 22
from collections import deque


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_cards(data):
    player1, player2 = data.split("\n\n")
    return deque(map(int, player1.splitlines()[1:])), deque(map(int, player2.splitlines()[1:]))


def play_cards(cards1, cards2):
    while len(cards1) and len(cards2):
        c1 = cards1.popleft()
        c2 = cards2.popleft()
        if c1 > c2:
            cards1.append(c1)
            cards1.append(c2)
        else:
            cards2.append(c2)
            cards2.append(c1)

    points = 0
    winner_cards = cards1 + cards2
    for i, value in enumerate(reversed(winner_cards)):
        points += (i+1) * value
    return points


def run():
    data = load_data("Day22.txt")
    cards1, cards2 = get_cards(data)
    print(play_cards(cards1, cards2))
