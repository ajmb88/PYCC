def get_city_country(city_name, country_name):
    """Print a simple statement about the city and country entered from input."""
    city_country = f"\n{city_name} is the name of a city, and {country_name} is the " \
                   f"name of a country. How crazy!!"
    print(city_country)

while True:
    print(f"\nIf you give me the name of a city and a country I will tell you that it "
          f"is a city and a country in a sentence.")

    cities_name = input("City name??: ")
    if cities_name.lower() == 'q':
        break

    counties_name =input("Country name??: ")
    if counties_name.lower() == 'q':
        break

    get_city_country(cities_name.title(), counties_name.title())
