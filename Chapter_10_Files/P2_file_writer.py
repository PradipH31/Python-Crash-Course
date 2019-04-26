#!../ENV/bin/python
# Writing files
# w is for write mode
# with open(filename, 'w') as var:
# var.write('text')
filename = './Files_to_work_with/test.txt'
with open(filename, 'w') as file_writer:
    file_writer.write('Hey\n')
    file_writer.write('Looking good')
# Writing multiple lines with \n escape
# Append mode is same as write with the argument a
