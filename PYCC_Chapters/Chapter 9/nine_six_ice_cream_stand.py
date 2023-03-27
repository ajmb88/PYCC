from _nine_one_restaurant_class import Restaurant as rest

class IceCreamStand(rest):
    """A class to represent an ice cream stand using the Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type, flavors = []):
        """
        Initialize the attributes of the parent class
        Then initialize attributes of the ice cream stand class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_ice_cream_flavors(self):
        """Print a list of ice cream flavors served"""
        print(f"\nWelcome to {self.name.title()}.  Here we serve the best {self.food} "
              f"in town.  Here are a list of our top sellers!!")
        for flavor in self.flavors:
            print(f"{flavor.title()}")

my_ice_cream = IceCreamStand("aaron's ice cream parlour", "ice crea, duh!",
                             ["chocolate", "rocky road", "bububle gum", "peppermint "
                                "crisp"])

my_ice_cream.print_ice_cream_flavors()

other_ice_cream = IceCreamStand("Other guys spot", "frozen shit cream", ["Greasy soda",
                                "pinapple and wood", "beach towel mango", "pepperoni "
                                "and lemon", "hot sauce, wine, and catnip"])

other_ice_cream.describe_restaurant()
other_ice_cream.open_restaurant()
other_ice_cream.print_ice_cream_flavors()
