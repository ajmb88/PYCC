from random import choice

possible_choices = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, "A", "B", "C", "D", "E",
                    "F", "g"]
winning_choices = []

for items in range(8):
    item = choice(possible_choices)
    winning_choices.append(item)
    possible_choices.remove(item)


print(f"\nThe winning characters are:")
for picks in winning_choices:
    print(picks)

