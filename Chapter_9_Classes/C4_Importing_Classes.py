#!./ENV/bin/python
# ----------------------------------------------------------------
# Importing a single class from module
# from module_name import Class
# Multiple classes can be stored in a module

from C1_Book import Book

new_book = Book("NS python", 1990)
print(new_book.get_name())
