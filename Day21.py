# AOC20 day 21


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def parse_foods(data):
    foods = []
    for line in data.splitlines():
        ingredients_part, allergens_part = line.split(" (contains ")
        ingredients = ingredients_part.split()
        allergens = allergens_part[:-1].split(", ")
        foods.append([ingredients, allergens])
    return foods


def find_dangerous_ingredients(foods):
    allergen_options = dict()
    dangerous_ingredients = dict()
    for food in foods:
        if len(food[1]):
            for allergen in food[1]:
                if allergen in allergen_options:
                    allergen_options[allergen].intersection_update(food[0])
                else:
                    allergen_options[allergen] = set(food[0])
    updates = 1
    while updates:
        updates = 0
        for allergen in allergen_options.keys():
            if len(allergen_options[allergen]) == 1:
                dangerous_ingredients[allergen] = list(allergen_options[allergen])[0]
                for a in allergen_options.keys():
                    allergen_options[a].discard(dangerous_ingredients[allergen])
                updates += 1
                break
    return dangerous_ingredients


def count_safe_ingredients(foods, dangerous_ingredients):
    count = 0
    for food in foods:
        count += len([ingredient for ingredient in food[0] if ingredient not in dangerous_ingredients.values()])
    return count


def run():
    data = load_data("Day21.txt")
    foods = parse_foods(data)
    dangerous_ingredients = find_dangerous_ingredients(foods)
    print(count_safe_ingredients(foods, dangerous_ingredients))
