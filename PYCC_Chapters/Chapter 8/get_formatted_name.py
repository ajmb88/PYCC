def get_formatted_name(first_name, last_name, middle_name = ''):
    """ Enter first and last name. Return full name."""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()

actor = get_formatted_name('tommy', 'cruismore')
print(actor)

musician = get_formatted_name('jonny', 'bravo', 'meathead')
print(musician)