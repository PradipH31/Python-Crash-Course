#!./ENV/bin/python
# ----------------------------------------------------------------


class Car():
    """Class for a car"""

    def __init__(self, model, year):
        """Initialize the car"""
        self.model = model
        self.year = year

    def get_desc_name(self):
        """Get the descriptive name of the car"""
        return (str(self.year) + self.model)


class ElectricCar(Car):
    """Class from car class"""

    def __init__(self, model, year, batt_size):
        """initialize the electric car"""
        super().__init__(model, year)
        self.batt_size = batt_size

    def get_batt(self):
        """returns the battery"""
        return self.batt_size

    def get_desc_name(self):
        """Get the descriptive name of the car"""
        return ("Electric " + str(self.year) + self.model)
