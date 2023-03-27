from car import Car

my_car = Car('Hyundai', 'elantra', '2016')

print(my_car.get_descriptive_name())

my_car.odometer_reading = 156

my_car.get_odometer_reading()