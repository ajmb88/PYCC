class Users:
    """Create a class that will print infomation about a user"""
    def __init__(self, first_name, last_name, D_O_B, workplace, age,):
        """Initialize information about the user."""
        self.fn = first_name
        self.ln = last_name
        self.dob = D_O_B
        self.wp = workplace
        self.age = age
        self.full_name = (self.fn + " " + self.ln)
        self.login_attempts = 0



    def print_info(self):
        """Print all the info stored for the user."""
        print(f" First Name : {self.full_name.title()}, Date of Birth : {self.dob}, "
              f"Place pf Employment : {self.wp.title()}, Age : {self.age}.")

    def greet_user(self):
        """Print a message greeting the user."""
        print(f"Hello, {self.full_name.title()}.  Great to see you again. Heading out "
              f"to {self.wp.title()} I see.\n")

    def increment_login_attempts(self):
        """Increase the login_attempt counter by 1 each time its used."""
        self.login_attempts += 1
        if self.login_attempts == 1:
            print(f"{self.full_name.title()}, has attempted to login to this machine "
              f"{self.login_attempts} time.")
        else:
            print(f"{self.full_name.title()}, has attempted to login to this machine "
                  f"{self.login_attempts} times.")

    def reset_login_counter(self):
        """Resets the login counter back to 0."""
        self.login_attempts = 0
        print(f"{self.full_name.title()}'s login attempts have been reset to"
              f" {self.login_attempts}")



mike = Users('mike', 'nutter', 'sept.15,1943', 'mikes penis pumping service.', '43')
jenny = Users('jenny', 'jenson', 'june.18.2001', 'mikes penis puming service.', '28')
salim = Users('salim', 'salami', 'april,23,1988', 'cats cradle animal shelter.', '74')


print(mike.full_name.title())
mike.print_info()
mike.greet_user()

print(jenny.full_name.title())
jenny.print_info()
jenny.greet_user()

print(salim.full_name.title())
salim.print_info()
salim.greet_user()

mike.increment_login_attempts()
mike.increment_login_attempts()
mike.increment_login_attempts()
mike.increment_login_attempts()
mike.reset_login_counter()
mike.increment_login_attempts()
mike.increment_login_attempts()
