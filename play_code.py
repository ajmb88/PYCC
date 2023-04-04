filename = 'Downloading_Data/data/pi_million_digits.txt'
class Fib:
    '''Trying to make a class to display fibbonacci sequence.'''

    def __init__(self):
        
        
        self.fib = [1,1]


    def check_bday(self, bday):
        self.bday = bday
        for i in range(10000):
            x = self.fib[-1] + self.fib[-2]
            self.fib.append(x)
        
    
        if self.bday in self.fib:
            print('yes')
        else:
            print('no')

Fib().check_bday(9231988)
Fib().check_bday(1)

class Pi_Check:
    ''' Checking the first million digits of pi for certain values.'''

    def __init__(self):

        self.pi_string = ''
        with open(filename) as f:
            self.lines = f.readlines()

            
            for self.line in self.lines:
                self.pi_string += self.line.rstrip()

    def print_pi(self, val):
        '''Printing the first amount of pi digits.'''
        print(f"{self.pi_string[:val]}")

    def bday_pi_check(self, bday):
        ''' method to see if your bday is in the first one million digits of pi.'''
        self.bday = bday
        if self.bday in self.pi_string:
            print(f"Your bday: {bday} is in the first one million digits of pie. You lucky bastard! ")
        else:
            print(f"Nope, nothing here, you suck.  Sorry!")


pie = Pi_Check()
pie.print_pi(40)
pie.bday_pi_check('23245235631')