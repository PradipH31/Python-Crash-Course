#!./ENV/bin/python
# ----------------------------------------------------------------
# Classes from a module
# from module_name import ClassName, ClassName2
from C2_Inheritance import Car, ElectricCar

not_electric = Car('Honda', 2010)
elec_car = ElectricCar('Tesla', 2000, 88)

print(not_electric.get_desc_name())
print(elec_car.get_desc_name())
