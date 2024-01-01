# Chapter 6: Looping through Dictionary
# Dictionary keys, only values, key and value

person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}

print("Default case >> Looping through Keys only: option1")
for key in person1:
    print(key)

print()
print("Default case >> Looping through Keys only: option2")
for key in person1.keys():
    print(key)

print()
print("Looping through Values only: option1")
for value in person1.values():
    print(value)

print()
print("How to get the value of the key?")
for key in person1.keys():
    print(">> key in this iteration is: ",key)
    print(">> value in this iteration is: ", person1[key])

print()
print("Looping through Keys and Values (mostly used), items()")
for key, value in person1.items():
    print('>> key in this iteration is: ', key)
    print('>> value in this iteration is: ', value)

print()
# Exercise 6-5:
rivers_countries = {'nile': 'egypt',
                    'amazon': 'brazil',
                    'volga': 'russia',
                    'mississippi': 'usa',
                    'thames': 'uk'}
print("######## Exercise 6-5--------------------- ")
print("# 1. Use a loop to print a sentence about each river.")
for river, country in rivers_countries.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()
print("# 2. Use a loop to print the name of each river.")
for river in rivers_countries.keys():
    print(f"The river {river.title()}.")

print()
print("# 3. Use a loop to print the name of each country.")
for country in rivers_countries.values():
    print(f"The country {country.title()}.")