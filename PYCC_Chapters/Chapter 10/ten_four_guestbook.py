flag = True

while flag:
    name = input(f"\nHello, what is your name? press 'Q' to quit at any time: ")
    if name.lower() == "q":
        flag = False
    else:
        with open("Guest_book", 'a') as file:
            file.write(f"\n{name.title()}")
