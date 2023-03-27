from random import randint

class Die():
    """A class to represent a single die"""

    def __init__(self, sides = 6):
        """Initialize the Dice class."""
        self.sides = sides

    def roll_die(self):
        """Returns a random number between 1 and the number of sides on the die."""
        return randint(1, self.sides)

    def print_die_roll(self):
        """Print the result of the die roll"""
        number = randint(1, self.sides)
        print(number)


d23 = Die(23)
results = []
for roll_num in range(10):
    result = d23.roll_die()
    results.append(result)
print(results)

d23.print_die_roll()