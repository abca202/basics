## Chaper 7. User INPUT and WHILE LOOP
## While loop

# name = 'john'
# while  expression:
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration

# Be cautious of INFINITE loop.
# To avoid infinite looping make sure the looping condition changes with each iteration.


## Example

# num = 5
# while num < 10:
#     print(f"Num is still less than 10, '{num}'")
#     num +=1 # >> necessary condition to avoid infinite looping; if 'while' condition is negative than looping must be increasing
# print()


# num1 = 4
# while num1 > 1: # 'num1' is greater than 1 (TRUE) and is equal to 4
#     print(f"Num1 is still greater than 1, '{num1}'")
#     num1 -= 1 ## this will result in '4','3','2'.
# print()
#
# while num1 < 7: # 'num1' is less than 7 (TRUE) and is equal to 4
#     print(f"Num is still less than 7, '{num1}'")
#     num1 += 1 ## this will iterate from 1 to 6.
# print()

# while num1 < 7: # 'num1' is less than 7 (TRUE) and is equal to 4
#     print(f"Num is still less than 7, '{num1}'")
#     num1 += 2 ## this will result in '1','3','5'.
# print()

# print("\t GAME IS STARTING \t ----------->>>> ")
# name = ""
# while name.lower() not in ['exit', 'x', 'close']:
#     name = input("Enter your name: ")
#     print(f"Hello {name.title()}! Welcome to the Game!")
# print("Game is over! Good bye!")

print("-------------- Fuzz Buzz example with WHILE loop --------------------")
answer = '' ## empty variable
while answer.lower() != 'n': ## n==n -> True; n!=n -> False; y!=n -> True; ''!=n -> True
## 'while answer.lower() !=n >> means that when you run the code and after getting first loop result
##    (either Fuzz or Buzz or FuzzBuzz or 'else' result) than code will ask 'Do you want to continue? y/n:'
##       >> here if you answer 'y' which is "!='n' " than the code will be executed again
    num = int(input('Please enter any number:'))
    if num != 0:
        if num % 3 == 0 and num % 5 == 0:
            print('FuzzBuzz')
        elif num % 3 == 0:
            print('Fuzz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print("This is not dividable by 3 or 5.")
    else:
        print("Please enter a different number")
    answer = input("Do you want to continue? y/n:")
