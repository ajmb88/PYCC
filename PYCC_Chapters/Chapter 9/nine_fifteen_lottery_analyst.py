from random import choice


my_picks = ['A', 'B', '7', '2']
winning_picks = []
loto_count = 0
pick_amount = len(my_picks)

flag = True

while flag:
    lottery_choices = ["1", "2", "3", "4", "5", "6", "7",
                        "A", "B", "C", "D",]
    for item in range(pick_amount):
        loto_pick = choice(lottery_choices)
        winning_picks.append(loto_pick)
        lottery_choices.remove(loto_pick)
        if my_picks == winning_picks:
            match = "yes"
        else:
            match = "no"
        if my_picks == winning_picks:
            flag = False
    print(f"Winning characters: {winning_picks},  Loto Count: {loto_count}, ....{match}")
    winning_picks = []
    loto_count += 1




