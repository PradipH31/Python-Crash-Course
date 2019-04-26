#!../ENV/bin/python
# Reading files
# with open(file_name/path) as var(reader_file)
# var2 = var.read()
# with keyword ensures that python will close the file after use
# open opens the file in its arguments
# file_obj = open('./Files_to_work_with/pi_digits.txt')
with open('./Files_to_work_with/pi_digits.txt') as file_obj:
    contents = file_obj.read()
    print(contents)

# Reading line by line with for in
with open('./Files_to_work_with/pi_digits.txt') as file_object:
    # Making a list from a file data
    lines = file_object.readlines()
    a = 1
    for cont in file_object:
        # print('{} is gamer').format(a)
        print(f'Line {a} : {cont.strip()}')
        a += 1
print(lines)

# Working with data from a file
text = ''
for line in lines:
    text += line.strip()
print(text)
print(len(text))

# The data from the file can be treated as any other string data.
