from nine_three_users import Users as users

class Admin(users):
    """An admin class that inherits attributes of the Users class."""

    def __init__(self, first_name, last_name, D_O_B, workplace, age, privileges = []):
        """
        Initialize attributes of the parent class
        the initialize attributes of the child class.
        """
        super().__init__(first_name, last_name, D_O_B, workplace, age)
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nThe user {self.full_name.title()} has Administrator access. They have "
              f"the following permissions:")
        for item in self.privileges:
            print(item)

aaron = Admin("aaron", "brazier", "spet.23.1988", "thales", "33", ["Can add post.",
               "Can delete posts.", "Can remove users.", "Can modify website.",
               "Can deny access."])

aaron.show_privileges()