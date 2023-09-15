# import os
# # Create a file in write mode and add dada in it
# with open("test.txt", "w") as f:
#     f.write("Hey there\n")
#     f.write("Hope you are doing well\n")
#     f.write("Thank you!!")
#
# # Read data from exiting file
# with open("test.txt", "r") as f1:
#     data = f1.read()
#     print(data)

# ----------------------------------------------------------
'''
Constructor : It is method who calls automatically for any object of class calls.

class Computer():

    def __init__(self):
        print("Constructor")

    def config(self):
        print("RAM:8GB, CPU:4, SSD:512GB")
#create obj of class
comp = Computer()

#call the method of class
comp.config()

'''

# ---------------------------------------------------------------------------
'''
Errors:
Compile errors : syntax errors : missing parenthesis, missing a semicolon, utilizing undeclared variables,
runtime errors : name errors(incorrect attribute name), type errors(user trying to add string and int ), 
                    index errors(list have 4 element and user using index 4)
logical errors : 2+2 = 5 
attribute errors: string.reverse() ('str' object has no attribute 'reverse')


try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("The result is:", y)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
'''
# ------------------------------------------------------------------------------