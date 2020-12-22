# AOC20 day 22
from collections import deque


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def get_cards(data):
    player1, player2 = data.split("\n\n")
    return deque(map(int, player1.splitlines()[1:])), deque(map(int, player2.splitlines()[1:]))


def score(cards1, cards2):
    return sum((i + 1) * v for i, v in enumerate(reversed(cards1))), sum((i + 1) * v for i, v in enumerate(reversed(cards2)))


def play_combat(cards1, cards2):
    while len(cards1) and len(cards2):
        c1 = cards1.popleft()
        c2 = cards2.popleft()
        if c1 > c2:
            cards1.append(c1)
            cards1.append(c2)
        else:
            cards2.append(c2)
            cards2.append(c1)
    return score(cards1, cards2)


def play_recursive_combat(cards1, cards2):
    seen = set()
    while len(cards1) and len(cards2):
        # infinite loop prevention
        state = tuple(list(cards1) + [0] + list(cards2))
        if state in seen:
            return 1, 0
        else:
            seen.add(state)

        c1 = cards1.popleft()
        c2 = cards2.popleft()
        if len(cards1) >= c1 and len(cards2) >= c2:
            result = play_recursive_combat(deque(tuple(cards1)[:c1]), deque(tuple(cards2)[:c2]))
            wins1 = result[0] > result[1]
        else:
            wins1 = c1 > c2

        if wins1:
            cards1.append(c1)
            cards1.append(c2)
        else:
            cards2.append(c2)
            cards2.append(c1)

    return score(cards1, cards2)


def run():
    data = load_data("Day22.txt")
    cards1, cards2 = get_cards(data)
    print(play_combat(cards1, cards2))
    cards1, cards2 = get_cards(data)
    print(play_recursive_combat(cards1, cards2))
