# Chapter 6: Dictionary CRUD
# each element has a key(unique) and value(multiple) pair
# uses a hashing method, does not use index number like 'List', order of the keys is not guaranteed
# dictionary may include list if_statement multiple vales are needed for one key

print(f"# CREATing a Dictionary")
# Creating an Empty Dictionary: using '{key and value}' symbol
sample1 = {}
sample2 = dict()

person1 = {'name': 'john doe',
           'age': 25,
           'location': 'ny'
           }
print(person1)

print()
print(f"# READing = accessing a dictionary by using 'key' only")
print(f"getting the name of 'person1': {person1['name']}")
print(f"getting the age of 'person1': {person1['age']}")
print(f"getting the location of 'person1': {person1['location']}")

print()
print(f"# UPDATing = adding/modifying a dictionary")
person1['phone'] = '(123) 555-5555'
print(f"updated the dictionary by adding a new key-value pair 'phone': {person1}")
# phone does not exist in the initial dictionary; therefore it adds a new key-value pair (element)
person1['age'] = 30 # updating a key
print(f"updated the existing key 'age' with the new value: {person1}")

# person1 = {'name': 'john doe',
#            'age': 25,
#            'location': 'ny',
#            'phone': '(123) 555-5555'
#            }

print()
print(f"Dictionary may contain a 'list' as a value")
print(f"adding a new key-value pair where value is a list")
person1['cars'] = ['toyota', 'honda', 'bmw', 'subaru', 'merc']
print(f"added a new key 'cars' with a list as a value: {person1}")

# person1 = {'name': 'john doe',
#            'age': 25,
#            'location': 'ny',
#            'phone': '(123) 555-5555',
#            'cars': ['toyota', 'honda', 'bmw', 'subaru', 'merc']
#            }

print()
print(f"updating list-value of the 'cars' key inside the dictionary:")
person1['cars'][3] = 'chevy'
print(f"updated list substituting 'subaru' by 'chevy': {person1}")

print()
print(f"Another way of using a 'list' as a value of the key is to create a list first and then add it to the dictionary")
languages_list = ['eng', 'rus', 'kor', 'uzb']
person1['languages'] = languages_list
print(person1)

# languages_list = ['eng', 'rus', 'kor', 'uzb']
# person1 = {'name': 'john doe',
#            'age': 25,
#            'location': 'ny',
#            'phone': '(123) 555-5555',
#            'cars': ['toyota', 'honda', 'bmw', 'subaru', 'merc'],
#            'languages': languages_list
#            }




print()
print(f"DELETing a dictionary by using 'del' function")

