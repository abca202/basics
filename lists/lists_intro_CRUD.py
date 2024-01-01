# Chapter 3. Introducing Lists

## LIST is a data structure that can hold a multiple values in a single variable
message = "hello world" ## 'message' is just a variable with a single value string 'hello world'
friend = "john" ## 'friend' is just a variable with a single value string 'john'
number = 23 # 'number' is just a variable with a single value integer 23

# empty_list = []
messages = [message, "wow", "ok", "nice"] ## 'messages' is a variable which holds a multiple values in the square brackets and becomes a list
friends = [friend, 'obama', 'trump', 'biden']
numbers = [number, 11, 41, 57, 99]
#
# # Access, update, add element, remove element
# print(messages[0])
# print(messages[1])
# print(messages[-1])
#
#### Updating a list:
# print('original list', friends)
# friends[0] = "clinton"
# print('updated list', friends)
#
##### Adding a new element: append or insert
#### APPEND function - adds a new element IN THE END of the list always: list.append('element')
# print('old friends list', friends)
# friends.append('bush')
# print('appended friends list', friends)
#
#### INSERT function - adds a new element by index in the list: list.insert[index, 'element']
# print('old friends list', friends)
# friends.insert(2, 'regan')
# print('inserted list of friends', friends)
#
# # finding the index number for the given element
# print("what is the index of the element 'trump'?", friends.index('trump'))
#
# # finding the element value for the given index
# print("what is the value of the index '4'?", friends[4])
#
# test = [] ## empty list
# # test.insert('sample') ## incorrect syntax
# test.insert(4,'sample')
# print(test)
# print(test.index('sample')) ## "what is the index of the element 'sample'?"
# #
#


## Chapter 3: page 42 - Removing an Item in the List
# print("Chapter 3: page 42 - Removing an Item")

#### DEL statement/function: del listname[index] ## deleting an element by using index number
# print('Del statement: del list[index]')
cars = ['toyota', 'nissan', 'tesla', 'honda']
# print("original list of cars: ", cars)
# del cars[2]
# print(cars)

#### POP statement/function - removes an element but saves in the temp memory: cars.pop('index optional)
# print("POP statement - removes an element but saves in the temp memory: cars.pop('index optional')")
# cars.pop() # removes the LAST element in the list
# # cars.pop(2) # removes the specific element by index number
# print(cars)
#
# cars.append('subaru')
# print("added a new car to the list using 'append': ", cars)
#
# # creating a new list using POP function
# # deleted_cars = cars.pop()
# deleted_cars = cars.pop(1)
# print(cars)
# print('pop deleted an item by index 1 and created a new list from deleted element: ', deleted_cars)
# print(cars)


# # Functions (arg1, arg2,...) >> to do something action >> Return a value/list/
#

# cars.insert(0, 'mazda')
# cars.append('mercedes')
# cars.append('kia')
# print(cars)

## REMOVE function by using a value
# print("Removing an item by value")
# cars.remove('subaru') # removes the element by value
# cars.insert(2, 'kia') # added another 'kia' element in the list
# print(cars)
# cars.remove('kia') # removes the first occurrence of the identical element >> two 'kia' >> deleted the first 'kia' in the list
# print(cars)









