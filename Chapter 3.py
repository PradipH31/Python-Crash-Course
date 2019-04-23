#!./ENV/bin/python
# ----------------------------------------------------------------
# Lists:
bicycles = ['BMX', 'Duke', 'KTM', 'Pulsar']
print(bicycles)
print(bicycles[2].title())

# last element can be accessed by index -1
# second from the last element by index -2
print(bicycles[-1])

message = "My first bike was a " + bicycles[-2] + "."
print(message)

# changing value of elements of a list
bicycles[2] = "Platinum"

# adding elements
bicycles.append('Ducati')

# inserting data at a specific index
bicycles.insert(0, "R15")

# deleting data from the list
del bicycles[3]

# deleting the last element of the list
# the method pop is static and causes change
# to the object it is applied to

# prints the elements of bicycles without the last element

# the variable containing the output of pop will have the last element
popped_bike = bicycles.pop()
print(bicycles)
print(popped_bike)

# pop can be used with index as a parameter

# deleting elements by value
bicycles.remove('BMX')
print(bicycles)

# Rule of hand is to name lists in plural form

# Sorting a List:
cars = ["Toyota", "Honda", "Suzuki", "BMW"]
cars.sort()
print(cars)

# Sorting in reverse order:
cars.sort(reverse=True)
print(cars)

# Temporary Sorting:
print(sorted(cars))

# Reversing a list:
cars.reverse()
cars.reverse()
print(cars)

#  Length of a list:
print(len(cars))
# ----------------------------------------------------------------
