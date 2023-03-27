class Restaurant:
    """A representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing the class."""
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        """Quick sentence describing the restaurant."""
        print(f"\nThe restaurant, {self.name.title()}, is now open for "
              f"business. The food here is {self.food.title()}. Dont like it, "
              f"Dip.")

    def open_restaurant(self):
        """Print a message saying the restaurant is open."""
        print(f"\n"
              f"{self.name.title()} is now open to serve the best "
              f"{self.food.title()} food in town.")

foods = Restaurant("Bambi BBQ", "Deer Ribs")

print(foods.name)
print(foods.food)

food1 = Restaurant("KFC", "Cancer Tumors")

food1.describe_restaurant()
food1.open_restaurant()