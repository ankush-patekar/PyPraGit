import os

with open("test.txt", "w") as f:
    f.write("Hey there\n")
    f.write("Hope you are doing well\n")
    f.write("Thank you!!")


with open("test.txt", "r") as f1:
    data = f1.read()
    print(data)
