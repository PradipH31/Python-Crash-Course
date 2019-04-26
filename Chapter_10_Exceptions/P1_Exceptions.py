#!../ENV/bin/python
# ----------------------------------------------------------------
# ZeroDivisionError Exception
a = 5
try:
    b = a / 0
except ZeroDivisionError:
    print("You can't divide by zero")

# Using try except for exception handling
# Using the else block executes if the code in try block does not cause any
# exceptions So try block should contain only the code that can cause exception
try:
    b = a / 2
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print(b)

# FileNotFoundError Exception
filename = 'a.abc'
try:
    with open(filename) as fil:
        fil.read()
except FileNotFoundError:
    print(f'{filename} does not exist')


# Analyzing text:
def word_count(f_name):
    try:
        with open(f_name) as f_reader:
            contents = f_reader.read()
    except FileNotFoundError:
        print(f"File {f_name} not found")
    else:
        print(f"There are {str(len(contents.split()))} words in {f_name}")

# Working with multiple files:
filenames = [
    'alice.txt', 'siddhartha.txt', 'moby_dick.txt',
    '../Chapter_10_Files/Files_to_work_with/pi_digits.txt'
    ]
for file_n in filenames:
    word_count(file_n)
# Failing silently
# Using pass in exception error will not display anything for the case


def word_count_no_message(f_name):
    try:
        with open(f_name) as f_reader:
            contents = f_reader.read()
    except FileNotFoundError:
        pass
    else:
        print(f"There are {str(len(contents.split()))} words in {f_name}")
# Logging


def word_count_no_message_log(f_name):
    try:
        with open(f_name) as f_reader:
            contents = f_reader.read()
    except FileNotFoundError:
        with open("log.txt", 'a') as error_file:
            error_file.write(f"The file {f_name} does not exist.")
    else:
        print(f"There are {str(len(contents.split()))} words in {f_name}")

filenamed = [
    'alice.txt', 'siddhartha.txt', 'moby_dick.txt',
    ]
for file in filenames:
    word_count_no_message_log(file)
