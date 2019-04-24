#!./ENV/bin/python
# ----------------------------------------------------------------
# User Input requires a prompt
u_name = input("Enter username: \n")
users = {
    'user1': {
        'u_name': u_name
    }
}
print(users)

# Input is stored as string.
# Explicitly convert to use
# int(input())
user_height = 0
while user_height < 3:
    user_height = int(input("Enter your height:\n"))
    print("tall")

# While Loop
# Use of !=
a = 0
while a <= 10:
    print(a * 2)
    a += 1

# Use of flags:
ab = True
a = -1127
while ab:
    print(a)
    if a < 60:
        ab = False

# Using break to exit the iteration
# Using continue goes to next iteration without executing following statements

# Moving items from one list to another with while
experiment_medicines = ['ABC', 'DCS', 'LKS', 'LAKSD', 'cat', 'cat']
approved_medicines = []
while experiment_medicines:
    approved_medicine = experiment_medicines.pop()
    print("Approved " + str(approved_medicine))
    approved_medicines.append(approved_medicine)
print(experiment_medicines + approved_medicines)

# Removing all instances from a list
while 'cat' in approved_medicines:
    approved_medicines.remove('cat')
