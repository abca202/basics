# Chapter 5: IF Statements (04/09/2022 lecture)

num = 5 # setting the value, defining/assigning
# num == 5 # we are comparing the value of num to 5, returns True
# num == 4 ## we are comparing the value of num to 4, returns False
# print("value of 'num' is ", num)
# ## Expression to generate True/False condition
# print(f"expression 'num==5' is {num==5} because 5==5") # True because above num=5 = 5
# print(f"expression 'num==4' is {num==4} because 5!=4") # False because above num=5 is not equal to 4
# print(f"expression 'num > 4' is {num > 4} because 5 > 4") # True because num=5 > 4
# print(f"expression 'num < 4' is {num < 4} because 5 is not < 4") # False because num=5 is not less than 4
# print(f"expression 'num <> 4' is {num != 4} because 5 is not = 4") # True because num=5 is not equal to 4
# print()

favs = list(range(10,21)) # list of numbers from 10 to 20
# print("num is in favs?", num in favs) # is 5 in the favs range? >> NO, 5 is not in the favs rang(10,21)>> False
# print("num is not in favs?", num not in favs) # 5 is not in the favs range? >> correct, 5 is not in the favs range(10,21) >> True
# print()
#
keyword = 'abrakadabra'
# print('keyword is', keyword)
# print("letter 'e' in the 'keyword'?", 'e' in keyword)

# IF condition:
#   code block, when condition is true
# Else:
#   code block, when condition is false

# print('num is', num)
# if num > 4:
#     print("Num is greater than 4...if condition is satisfied")
#     print("Do something because num is greater than 4")
# else:
#     print("Num is either equal or less than 4")
# print()

num = 4 # assigning a new value for variable 'num'
# print('num is', num)
#
# if num > 4:
#     print("Num is greater than 4...")
#     print("Do something because number is greater than 4")
# else:
#     print("Num is either equal or less than 4.. else condition is satisfied")
# print()

# bank account, account balance, money transfer
# if_statement bal <= transfer amount:
#   than notify me
# else:
#   execute the transfer

## ELIF condition: it can be used only after IF condition and before ELSE condition.
num > 4 # this is NOT assigning a new value! >> '>' sign doesn't do any operation in this string
# if num > 4: # required starting statement
#     print("Num is greater than 4...") # above we assigned a new value to the 'num' which is 4; therefore, 'elif' condition is satisfied
#     print("do something if_statement greater than 4")
# elif num == 4: # optional statement
#     print("Num is equal to 4") # condition satisfied and it will stop here
# else: # optional statement
#     print("Num is either equal or less than 4") # this condition will not be executed because 'elif' is satisfied
# print()

cars = ['audi', 'bmw', 'subaru', 'toyota']
# print('list of cars:', cars)
# for car in cars: ## it will loop through each element in the list and apply 'if' or 'else' conditions
#     if car == 'bmw': ## 'if' condition will be applied after 'else' because 'bmw' is second in the list
#         print("the list contains 'bmw'>>>", car.upper())
#     else: # 'else' condition will be applied first because 'audi' is the first in the list
#         print("just a car >>>", car)
# print()

# Problem-solving question:
# 1.'Input' problem >> message accepting
# msg = input("Enter your number here: ") # the result of input is always a string
# print("you entered: ", msg)
## if msg == 'a':
##        pass
# print()


## 2. Vowels
# yes or no answer if_statement the phrase contains vowels (a,e,i,o,u)
# msg = input("Enter your phrase here: ")
# print("you entered: ", msg)

## Code writing process:
# a. pseudocode
# b. create a list (vowels phrase)
# c. loop the 'msg' for each character
# d. check if each character is in the vowels(list)
# e. when we see the vowels print "You have vowels in the phrase"
# f. then Stop the looping process by using 'break' function
# g. print "Program is completed"

# msg = input("Enter your phrase here: ")
# print("you entered: ", msg)

vowels = 'aeiou'
# for letter in msg:
#     if letter.lower() in vowels:
#         print("You have vowels in the phrase")
#         break # no more looping if_statement code reached this line
#     else:
#         print("Your phrase does not have a vowel.")
# print("Searching process completed.")

# hw: print the number of vowels in the phrase
# age = 30
# age = age + 2 == age += 2 >> 32
# age = age - 1 == age -= 1 >> 31

# print()
# vowels = 'aeiou'
# vowel_count = 0
# for letter in msg:
#     if letter.lower() in vowels:
#         # print("You have vowels in the phrase")
#         vowel_count +=1
#     else:
#         # print("Your phrase does not have a vowel.")
#         pass
# print(f"you have {vowel_count} vowels in your phrase.")
# print("Searching process completed.")

## Swapping the values:
a = 456
b = 789
print(a,b)
# ## how to swap the values of variable a and b
# c = a ## c is a temp variable
# print(a, b)
# a = b
# b = c
# print(a,b)


## another way to swap values >> python way
# a, b = b, a
# print(a, b)

## 1. Additional to the 'Vowels' execersie

# msg = input("Enter your phrase here: ")
# print("you entered: ", msg)
#
# my_numbers = '678'
#
# for my_number in msg:
#     if my_number in my_numbers:
#         print("You have my_numbers in the line")
#         # break
#     else:
#         print("There are no numbers in the phrase.")
# print("Process completed.")

## 2. Addition to the 'Vowels' exercise

# vowels = 'aeiou'
# not_found = 0 # not vowel
# found = 0 # vowel
#
# msg = input("Please enter your phrase:")
# print("you entered: ", msg)
#
# for letter in msg:
#     if letter.lower() in vowels:
#         found +=1
#         print("I found a vowels in your phrase {found} times.")
#     else:
#         not_found +=1
#         print("Your phrase does not have a vowel: {not_found} times.")
#
# print(f"This loop went through {msg.upper()} and found vowels: {found} times!\n" f" and did not found vowels: {not_found} times!\n" f" Total times: {found +not_found}")
# print("Searching process completed.")

## Exercise 4-6
# for num in range(1,21):
#     if num % 2 != 0:
#         print(f"Odd numbers: {num}")
#
# odd_num = list(range(1, 21, 2))
#

## Exercise 4-10 Slices


