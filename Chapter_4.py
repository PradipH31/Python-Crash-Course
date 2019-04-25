#!./ENV/bin/python
# ----------------------------------------------------------------
# Looping through a list:
cars = ["Toyota", "Honda", "Suzuki", "BMW"]
for car in cars:
    print(car)
# The indented code block is looped

# Range is a list of numbers
# ranging from 1st number to last number
# So it iterates for number of last arguments -1 times
a = list(range(1, 6))
print(a)

# The third argument to range function provides the increment value
print(range(1, 40, 4))

# Example:
squares = []
for number in range(1, 10):
    squares.append(number**2)
print(squares)

# Minimum Maximum and Sum
min(squares)
max(squares)
sum(squares)

# same as example:
squares = [number**2 for number in range(1, 10)]
print(squares)

# similar to example:
print([x**3 for x in range(1, 11)])

# Slicing a list with the index of a list:
names = ['Charles', 'Ben', 'Amir', 'Jake', 'Sarah', 'Murph', 'Ricky']
print(names)
print(names[1:3])
print(names[:4])
print(names[3:])
print(names[-3:])

# Loop through a slice:
for name in names[:4]:
    print(name.title())

# Copying a list: Don't provide index to the slice program
# New list cannot be created by referencing the existing list.
# It will only reference the object
# Any changes to the first list will be added to new one.
my_friends = names[:]
names.append('Pat')
print(my_friends)

# Tuples:
# 	The constant(immutable in python) lists are called tuples
# 	Tuples are same as lists except they cannot be changed and use parenthesis
year_of_birth = (60, 50)
print(year_of_birth)

# Tuple cannot be modified. A new value can be assigned to an existing tuple
year_of_birth = (20, 30, 40)
print(year_of_birth)
# ----------------------------------------------------------------
