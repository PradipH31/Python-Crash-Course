#!ENV/bin/python
# ----------------------------------------------------------------
# Conditionals: If statement
# Numerical comparison in if
cars = ["BMW", "Mercedes", "Lamborghini", "Toyota"]
for car in cars:
    if car == 'BMW':
        print(car.upper())
    else:
        print(car.lower())

# When case matters, use lower() function
req_toppings = "Cheese"
if req_toppings != "Cheese":
    print("Not my order")

# AND OR operators to check multiple conditions
if car == 'mercedes' and req_toppings == 'cheese':
    print(0)

# Checking if a list contains a certain item:
print('Mercedes' in cars)

# Checking if a list doesnot contain a certain item:
banned_users = ["Andrew", "Dave", "Felix"]
user = 'RacerBoy'
if user not in banned_users:
    print("Welcome")

# if elif else
# There can be multiple elif blocks and/or no else block
body_temperature = 98
if body_temperature < 98:
    print("Something is wrong")
elif body_temperature == 98:
    print("You are fine")
else:
    print("You have a fever.")

# To check for every condition,make different if blocks

# Check if a list is null or not:

if cars:
    print(cars)
else:
    print("Add cars")

# Multiple lists usage:
available_classes = [
    'Math', 'History', 'Science', 'English', 'Computer', 'Finance'
    ]
requested_classes = ['Japanese', 'Computer']
classes_enroll = 0
for r_class in requested_classes:
    if r_class in available_classes:
        print("Class " + r_class + "available.")
        classes_enroll += 1
print("Total classes to enroll = " + str(classes_enroll))
# ----------------------------------------------------------------
