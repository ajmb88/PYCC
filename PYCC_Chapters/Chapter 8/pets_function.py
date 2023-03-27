def describe_pet(animal_type, pet_name):
    """ Display message about a fake pet."""
    print(f"\nI have a pet {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}, Cool!")

describe_pet('dragon', 'tinker bell')

describe_pet('human', 'peter')