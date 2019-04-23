#!./ENV/bin/python
# ----------------------------------------------------------------
# Dictionaries
# Components of a dictionary are key and value
car_1 = {
    'company': 'Honda',
    'color': 'red'}
print(car_1['color'])
print(car_1)

# Adding new key & value to dictionary
car_1['height'] = 4
print(car_1)

# Empty Dictionary
# Add keys and values

# Modifying values of a key
car_1['color'] = 'yellow'
print(car_1)

car_1['speed'] = 22
increment_speed = 12
car_1['speed'] = car_1['speed'] + increment_speed
print(car_1)

# Removing key value pairs
del car_1['height']
print(car_1)

# Other Uses
fav_food = {
    'john': 'Pizza',
    'sarah': 'Ice-cream',
    'dan': 'Meatballs',
    'eugene': 'Spaghetti',
    'warren': 'Pizza'
}
print(
    "Eugene likes " + str(fav_food["eugene"]) + " very much."
)

# Looping through a Dictionary
# The first variable in the for loop should be the key & second should be value
for name, food in fav_food.items():
    print("\n" + str(name) + "'s favorite food is " + str(food))

# Looping through keys in a dictionary
# The dictionary loops through the keys by default
# So fav_food.keys() = fav_food
print("\nThe participants were:")
for participants in fav_food.keys():
    print("\n" + str(participants).title())
if "Jake" not in fav_food:
    print("Jake did not take the poll.")

# Looping through keys of a dictionary in order using sorted function
for participants in sorted(fav_food.keys()):
    print("\n" + str(participants).title())

# Looping through values of a dictionary
print("Mentioned foods:")
for food in fav_food.values():
    print(food)

# Avoid repeated values by using //set\\
# Values can be sorted as well
for food in set(fav_food.values()):
    print(food)

# Nesting
# Dictionary in a list
book_1 = {
    'cover': 'leather',
    'title': 'Javascript',
    'published_year': '2012',
    'author': 'H. Martin'
    }
book_2 = {
    'cover': 'wood',
    'title': 'Python',
    'published_year': '2022',
    'author': 'A. Gosen'
    }
book_3 = {
    'cover': 'plastic',
    'title': 'Java',
    'published_year': '2011',
    'author': 'H. Martin'
    }
books = [book_1, book_2, book_3]
for bok in books:
    print(bok)
for x in range(0, 5):
    book_new = {
        'cover': 'wood',
        'title': 'Go',
        'published_year': '2100',
        'author': 'No Starch'
    }
    books.append(book_new)
"""0 to -3 means 0 to 5"""
for bok in books[:-3]:
    if bok['cover'] == 'wood':
        bok['cover'] = 'black leather'
print(books)

# List in a dictionary
smartphone = {
    'company': 'Samsung',
    'features': ['250gb', 'GPS', 'Camera']
}
fav_lang = {
    'John': ['Japanese', 'English', 'Mandarin'],
    'Emma': ['Neplai'],
    'Mike': ['Korean', 'Portugese']
}

# Dictionary in a dictionary
users = {
    'pampered_dog': {
        'user_id': '0',
        'password': '1234',
        'user_name': 'pampro'
    },
    'hacksberg': {
        'user_id': '1',
        'password': '1234',
        'user_name': 'mhacko'
    }
}
