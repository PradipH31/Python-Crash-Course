#!./ENV/bin/python
# ----------------------------------------------------------------
# Importing module into a module
# This is similar to OOP from java where you put certain classes in one module
# and import it into another module
# (File)electric_car.py
# """A set of classes that can be used to represent electric cars."""
# from car import Car
# class Battery():
#     --snip--
# class ElectricCar(Car):
#     --snip--
# (File)car.py
# """A class that can be used to represent a car."""
# class Car():
#   --snip--
# (File)my_cars.py
# from car import Car
# from electric_car import ElectricCar
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())