#!../ENV/bin/python
# JSON module
# open file with with open command
# json.load(data, file_object)
import json

numbers = []
filename = 'numbers.json'
try:
    with open(filename) as num_reader:
        numbers = json.load(num_reader)
except FileNotFoundError:
    print(f"File {filename} not found")
else:
    print(numbers)
