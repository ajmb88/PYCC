""" A class that can be used to represent a car."""

class Car:
    """Simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initializing the car class."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Get a descriptive name of the car entered."""
        long_name = f"This car is a {self.year}, {self.make.title()} {self.model}.\n"
        return long_name

    def get_odometer_reading(self):
        """Get the reading from the odometer."""
        print(f"This car has {self.odometer_reading} kilometers on it.\n")

    def update_odometer(self, mileage):
        """Set the odometer reading to a certain value, can't go lower."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"Your mileage can't go down. Your current odometer reading is: "
                  f"{self.odometer_reading}, you tried to enter: {mileage}.")

    def increment_odometer(self, increment_amount):
        """A function used to increment the odometer by the amount entered."""
        if increment_amount >= 0:
            self.odometer_reading += increment_amount
        else:
            print(f"You can't increase your odometer by a negative number you cheat.")
