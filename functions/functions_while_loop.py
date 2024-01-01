## While_Loop function:

def while_loop_increment():
    """ Docstring - 'while_loop' when we are setting bottom limit in the condition, we need to increment
     : return """
    print("while loop when we are setting bottom limit in the condition, we need to increment")
    current_number = 1
    while current_number <= 2:
        print('current number: ', current_number)
        current_number = current_number + 1
#
#
def while_loop_decrement():
    print("while loop when we are setting bottom limit in the condition, we need to decrement")
    current_number = 1
    while current_number > 0:
        print('current number: ', current_number)
        current_number = current_number - 1

#
def fuzz_buzz():
    try:
        print("______ Fuzz Buzz example with While Loop __________")
        answer = ''
        while (answer.lower() != 'n') and (answer.lower() != 'no'):
            # n == n -> True, n != n -> False, y != n -> True, '' !=n -> True
            num = int(input('Please enter a number: '))
            # num = 3
            if num != 0:
                if num % 3 == 0 and num % 5 == 0:
                    print('FuzzBuzz!')
                elif num % 3 == 0:
                    print('Fuzz!')
                elif num % 5 == 0:
                    print('Buzz!')
                else:
                    print('This is not dividable by either 3 nor 5')
            else:
                print("please enter a different number other than '0'")
            answer = input("Do you want to continue? y/n: ")
    except (FileNotFoundError, TimeoutError, NameError) as err:
        print("error occurred:", err)

## Infinite loop !!!
# fuzz_buzz()
# while_loop_decrement()
# while_loop_increment()


