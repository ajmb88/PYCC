guest_name = input(f"\nHello, what is your name?: ")

with open('Guestbook', 'a') as file:
    file.write(f"\n{guest_name.title()}")