#!./ENV/bin/python
# ----------------------------------------------------------------
# Using instance of a class as an attribute for another class


class Car():
    """Class for a car"""

    def __init__(self, model, year):
        """Initialize the car"""
        self.model = model
        self.year = year

    def get_desc_name(self):
        """Get the descriptive name of the car"""
        return (str(self.year) + self.model)
# Default can be used in initiators for class


class Battery():
    """Battery class for electric car"""

    def __init__(self, battery_size=82):
        """Initialize the battery"""
        self.battery_size = battery_size

    def get_battery(self):
        """Return the battery"""
        return str(self.battery_size)


class ElectricCar(Car):
    """Class from car class"""

    def __init__(self, model, year):
        """initialize the electric car"""
        super().__init__(model, year)
        self.battery = Battery()

    def get_batt(self):
        """returns the battery"""
        return self.battery.get_battery()

    def get_desc_name(self):
        """Get the descriptive name of the car"""
        return ("Electric " + str(self.year) + self.model)

my_tesla = ElectricCar("Audi", 1990)
print(my_tesla.get_desc_name())
print(my_tesla.get_batt())
