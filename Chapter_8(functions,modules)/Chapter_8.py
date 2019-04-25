#!./ENV/bin/python
# ----------------------------------------------------------------
# Functions
# """   """ are docstrings & required by python to generate documentation


def greet(user_name, nick_name):
    """Displays a greeting"""
    print("Hello " + user_name)

# Keyword arguments - pair of parameters and values passed to function
greet(nick_name="Pradip", user_name="PrH31")

# Default Values
# Parameters with default values have to be listed at the last


def greet_me(user_name, nick_name="Nin6"):
    """Displays a greeting"""
    print("Hello " + nick_name)
greet_me(user_name="ac")

# Returning values


def get_formatted_name(first_name, last_name):
    """Return the full name in title form"""
    return (first_name + " " + last_name).title()

print(get_formatted_name(first_name="pradip", last_name="hamal"))

# Making an argument optional


def opt_example(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + middle_name + last_name
    else:
        full_name = first_name + last_name
    print(full_name.title())

# Returning a dictionary


def ret_dict(first_name, last_name):
    '''Returns a dictionary of the names'''
    return {'f_name': first_name, 'l_name': last_name}
print(ret_dict(first_name="pradip", last_name="hamal"))

# Using functions with loop(while)
# Passing a list to funcion
names = ['Pradip Hamal', 'Jake', 'Amir Blumenfeld', 'Str Cyd']


def list_names(param_names):
    '''Prints the contents of a list'''
    for name in param_names:
        print(name)
list_names(param_names=names)

# Modifying a list in a function
devices_wishlist = ['IPad', 'Mac', 'iWatch', 'iPhone', 'Razoe']
devices_owned = []


def mod_list(dev_list, dev_owned):
    '''Modifies the list'''
    while dev_list:
        device_owned = dev_list.pop()
        dev_owned.append(device_owned)
mod_list(devices_wishlist, devices_owned)
list_names(param_names=devices_owned)

# Preventing a function from modifying a list
# By supplying the function with a copy of the list i.e. list[:]
mod_list(devices_wishlist, devices_owned[:])
list_names(devices_owned)

# Arbitrary numbers of arguments
# Use of * makes a tuple for the arguments
# can also be used with positional arguments


def make_pizza(size, *toppings):
    '''Makes a pizza with any number of toppings'''
    print("Size " + str(size) + " pizza with toppings")
    print(toppings)
make_pizza(12)
make_pizza(10, 'Pepperoni', 'Cheese', 'Garlic')

# Using Arbitrary keyword arguments i.e. accepting key-value pair as input
# The ** creates an empty dictionary which accpets key=value pair


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics')
print(user_profile)


def build_book_data(**data):
    '''Build a book'''
    book = {}
    for key, value in data.items():
        book[key] = value
    print(book)
build_book_data(name="NoStarch Python")
