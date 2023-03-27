def build_person(first_name, last_name, age = None):
    """Build the profile fopr a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

actor = build_person('michael', 'jordan', '77')
print(actor)