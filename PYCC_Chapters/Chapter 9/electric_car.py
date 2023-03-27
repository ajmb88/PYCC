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


class Battery:
    """A simple atempt to model a battery for an electric car."""

    def __init__(self, battery_size=300):
        """Initialize the batteries attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KW battery.")

    def get_range(self):
        """Print a statement describing the range of the battery."""
        range = ((self.battery_size * 3.247) * 0.926)
        print(f"The range of this battery is {int(range)} Km at {self.battery_size}-KW")

class ElectricCar(Car):
    """Represent aspect specific to an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to this class
        """
        super().__init__(make, model, year)
        self.battery = Battery()




my_tesla = ElectricCar('tesla', 'model p', 1977)

print(my_tesla.get_descriptive_name())

my_car = Car("Hyundai", "Elantra", 2016)

print(my_car.get_descriptive_name())
my_car.get_odometer_reading()

my_car.odometer_reading = 23
my_car.get_odometer_reading()


my_car.increment_odometer(205116)
my_car.get_odometer_reading()

print(my_tesla.battery.describe_battery())

my_tesla.battery.get_range()