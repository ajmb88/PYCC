class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulates a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        """Simulate a dog rolling over on command."""
        print(f"{self.name.title()} rolled over.")

my_dog = Dog('Buddy', 44)

print(f"\nMy dogs name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.\n")

my_dog.sit()
my_dog.roll_over()

their_dog = Dog('roco', 3)

print(f"{their_dog.age}")