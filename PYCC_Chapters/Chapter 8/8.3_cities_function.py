def describe_cities(city, country):
    print(f"\nThe city of {city.title()} is located in the country of "
          f"{country.title()}. It's not that great, don't bother going.'")

describe_cities('paris', 'shitty france')

describe_cities(city='mississauga', country='top america')