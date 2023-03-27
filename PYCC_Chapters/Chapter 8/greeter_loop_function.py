
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name."""
    # variable to sore the full name.
    full_name = f"{first_name} {last_name}"
    # returns 'full_name' variable for recalling.
    return full_name.title()

# this is a loop function, ask for first and last name until 'q is pressed.
while True:
    print(f"\nPlease tell me your name:")
    print(f"Press 'Q' at anytime to quit.")

    f_name = input("First name: ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last name: ")
    if l_name.lower() == 'q':
        break

    # variable to store the information from the function and print results.
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}. Its nice to meet you.")