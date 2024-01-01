import yaml

try:
    # usual code to execute
    print('Executing a code in try block')
    # print(5/0)

    filepath1 = '../data/credentials.yml'

    # functions/steps
    with open(filepath1, "r") as stream:
        credentials = yaml.safe_load(stream)

    print("Try block execution completed :) ****")
except ZeroDivisionError as err:
    # executes only when ZeroDivisionError happens
    print("You can not divide by 0!")
    print("Printing the standard error:", err)
except FileNotFoundError:
    # executes only when FileNotFoundError happens
    print("Oops, no file no code execution")
except Exception as err:
    print("Printing the standard error", err)
finally: # you don't have to use this block
    # this block will be executed regardless exceptions happen or not
    print("clean up and close the browser.")

print("Execution completed !!!")

