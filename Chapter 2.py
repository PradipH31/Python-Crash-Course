#!./ENV/bin/python
# ----------------------------------------------------------------
# variables don't need to be declared
message = "Hello Python World"
print(message)

message2 = "Hello python crash course World"
message_the_third = 'Hey, I go by the name "POR"'
print(message.title())
print(message + "\n\t" + message2)
print(message_the_third)

# Stripping whitespaces
test1 = " Hey  "
print(test1)
print(test1.rstrip())
print(test1.lstrip())
print(test1.strip())
print(test1 == test1.rstrip())

# String functions
name = "Por is a good thing"
print("Hey " + name)
print(name.upper())
print(name.lower())
print(name.title())
print("Happy " + str(23) + "rd birthday")

# Math Functions
print(3 ** 2)

#  Zen of Python: import this in python terminal
# ----------------------------------------------------------------
