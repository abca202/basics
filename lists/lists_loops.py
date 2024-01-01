#### Chapter 4: Looping through the List
students = ['mike', 'tony', 'alice', 'jane']
## We can use 'PRINT' function to print each element of the list which creates REDUNDUNCY.
# print(f"Hello {students[0].title()}, welcome to the class!")
# print(f"Hello {students[1].title()}, welcome to the class!")
# print(f"Hello {students[2].title()}, welcome to the class!")
# print(f"Hello {students[3].title()}, welcome to the class!")
# print()

## Istead of the printing each element separately we can use 'FOR LOOP' function
#### FOR LOOP
# for tempvar in listname:
# some code to repeat

# for student in students:
#     print(f"Hello {student.title()}, welcome to the class!")

# for abc in students: # abc is a temp variable
#     print(f"Hello {abc.title()}, welcome to the class!")


places = ['hawaii', 'paris', 'bahamas', 'carribean']
# print(len(places))
## LOOPS to execute the code repetitively (what to loop and how many times)
# print("Looping through entire list: ")
# print(f"I want to visit {places[0].title()} next summer.")
# print()

# for var_each_element in list_name:
#     print(('lines of code to be repeated'))
# print()

# for place in places:
#     print(f"\n{place.title()} is a beautiful place.")
#     print(f"I want to visit {place.title()} next summer.")
# print()

##-----------------------------------------------------------------
#### RANGE(start, end, step) function, Working with list of numbers
## Default start is 0, don't include End, default step is 1
## range(5) >> 0 -> 4 ## 5 is not included
## range(2,6) >> 2 -> 5 ## 6 is not included
## range(4,16,3) >> 4,7,10,13 ## from 4 to 16 with step of 3

# print(range(5)) ## result: range(0,5)
# ## list() function is used to convert a range of numbers into a list
## numbers = list(range(5))
# print(list(range(5))) ## result: [0, 1, 2, 3, 4]

#### Exercise. PRINTING the range of numbers.

## Method 1. >> converting a range into a list
# nums = list(range(6)) ## range would be from 0 to 5; 6 will not be included
# for num in nums:
#     print(f"list of numbers from the range(6): {num}")
# print()

# ### Method 2. >> not using a 'list()' function
# for num in range(6):
#     print(f"list of numbers from the range(6): {num}")
# print()
#
# for num in range(1, 6):
#     print(f"list of numbers from the range(6): {num}")
# print()
#
#
# for num in range(1, 6, 2):
#     print(f"list of numbers from the range(6): {num}")
# print()

### Problem solving
## Ex.1. list all numbers between 21 and 36 that can be devided by 4
# for num in range(24, 37, 4):
#     print(f"range of numbers (21, 36) dividable by 4: {num}")
# print()

# ## Ex.2. looping a list the squares of numbers between 25 and 30 >> NO List created
# for num in range(25, 31):
#     print(f"list of squares of numbers between 25 and 30: num = {num} and square = {num**2}")
# print()

## Ex.3.
# 1.Creating an Empty List,
# 2.Looping through the range,
# 3.Appending numbers and their squares
# num_squares = []
# for num in range(25, 31):
#     # print(f"the number in the range of 25 and 31: {num}")
#     # print(f"square of this number is: {num**2}")
#     # print(f"square of this number is: {num**num}")
#     print(f"squares of numbers between 25 and 30: num = {num} and its square is: {num ** 2}")
#     num_squares.append(num ** 2)  ## adds results into the (empty)list
# print(f"final list of squares is: {num_squares}")
# print()

## Ex.3.2
nums = [8, 5, 6, 7, 2]
# nums_squares = []
# for num in nums:
#     print(f"each number: {num}")
#     print(f"square of this number is: {num**2}")
#     # print(f"square of this number is: {num**num}")
#     nums_squares.append(num**2)
# print(nums_squares)
# print()

# #### Positive and negative range of numbers
# negative_nums = []
# for num in range(5, -10, -2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()
#
# negative_nums = []
# for num in range(5, -10, 2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()

# negative_nums = []
# for num in range(-5, -10, 2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()
#
# negative_nums = []
# for num in range(-5, -10, -2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()

# negative_nums = []
# for num in range(5, 10, -2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()

# negative_nums = []
# for num in range(-5, 10, 2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()
#
# negative_nums = []
# for num in range(-5, 10, -2):
#     # print(num)
#     negative_nums.append(num)
# print(negative_nums)
# print()

# even_nums = []
# for num in range(100, 150, 2):
#     even_nums.append(num ** 2)
# print(even_nums)
# print()

## ----------------------------------------------
## Statistical functions:
# print("Statistical functions:")
# print("highest number 'max':", max(num_squares))
# print("lowest number 'min':", min(num_squares))
# print("sum of numbers 'sum':", sum(num_squares))
# print()

### SUM of all numbers in the list
# nums = [4, 2, 9, 10]
# print(nums)
# print(f"sum of nums: {sum(nums)}")
# print()
#
# sum = 0
# for num in nums:
#     sum += num
#     # sum = sum + num ## same as above
# print(f"sum of nums: {sum}")
# print()


