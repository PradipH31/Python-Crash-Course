#!../ENV/bin/python
# JSON module
# open file with with open command
# json.dump(data, file_object)
# Add exceptions
import json

numbers = [1, 22, 10, 76, 81]
filename = 'numbers.json'
with open(filename, 'w') as num_reader:
    json.dump(numbers, num_reader)
