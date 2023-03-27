def build_car(make, model, **car_info):
    """ Take info about a car and build a dictionary."""
    car_info['Make'] = make
    car_info['Model'] = model
    return car_info

my_car = build_car('Hyundai', 'Enlantra', Year= '2006', Price= '$20000', Seats= '5')

their_car = build_car('Hummer', "H2", Tow= 'Yes', Engine= 'V12', Smell= 'Shitty')


print(my_car)

print(their_car)
