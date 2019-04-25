# from module_name import function0_name, function1_name
# Using alias while importing to give name for function
# from module_name import function0_name as alias
# import module_name as alias
from Chapter_8 import make_pizza
from Chapter_8 import build_book_data as bbd
import Chapter_8 as C8
make_pizza(12, "Peppe")
bbd(name="Python Crash")
C8.list_names(C8.names)
