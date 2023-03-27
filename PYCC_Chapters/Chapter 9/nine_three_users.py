class Users:
    """Create a class that will print infomation about a user"""
    def __init__(self, first_name, last_name, D_O_B, workplace, age):
        """Initialize information about the user."""
        self.fn = first_name
        self.ln = last_name
        self.dob = D_O_B
        self.wp = workplace
        self.age = age
        self.full_name = (self.fn + " " + self.ln)



    def print_info(self):
        """Print all the info stored for the user."""
        print(f" First Name : {self.full_name.title()}, Date of Birth : {self.dob}, "
              f"Place pf Employment : {self.wp.title()}, Age : {self.age}.")
    def greet_user(self):
        """Print a message greeting the user."""
        print(f"Hello, {self.full_name.title()}.  Great to see you again. Heading out "
              f"to {self.wp.title()} I see.\n")

mike = Users('mike', 'nutter', 'sept.15,1943', 'mikes penis pumping service.', '43')
jenny = Users('jenny', 'jenson', 'june.18.2001', 'mikes penis puming service.', '28')
salim = Users('salim', 'salami', 'april,23,1988', 'cats cradle animal shelter.', '74')

""""
print(mike.full_name.title())
mike.print_info()
mike.greet_user()

print(jenny.full_name.title())
jenny.print_info()
jenny.greet_user()

print(salim.full_name.title())
salim.print_info()
salim.greet_user()

"""