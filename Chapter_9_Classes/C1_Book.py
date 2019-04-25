#!./ENV/bin/python
# ----------------------------------------------------------------
# # Classes


class Book():
    """Class for a book"""

    def __init__(self, name, year):
        """Initialize the book with name and year"""
        self.name = name
        self.year = year

    def get_name(self):
        """Returns the name of the book"""
        return self.name

my_book = Book("NOSP", "2012")
print(my_book.get_name())


class Car():
    """Car class"""

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.met_traveled = 0

    def set_met(self, m):
        if m > self.met_traveled:
            self.met_traveled = m

    def upd_met(self, m):
        self.met_traveled += m
my_car = Car("Toyota", "1999")

# Modifying attributes of an object directly through the variable
my_car.met_traveled = 20

# through a method
my_car.set_met(11)

# adding new value to the current value
my_car.upd_met(19)
