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

'''
import requests
import urllib3
import json
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# creating obj for session
s = requests.session()
# verify the server's TLS certificate
s.verify = False
# declare variable for uname and password
username = "Administrator@vsphere.local"
password = "Admin!23"
# Getting session ID for to authenticate followed api requests
session_id = s.post("https://172.17.41.44/rest/com/vmware/cis/session?~method=post", auth=(username,password))
# Getting all VM details(vm name, VMid, power_state)
vm_details = s.get("https://172.17.41.44/rest/vcenter/vm")
# VM info in json format
vm_info = vm_details.json()

# declare empty list to add VM ID
vm_id = []
for attr in vm_info["value"]:
    if attr["power_state"] == "POWERED_OFF":
        # print(attr["vm"])
        id = attr["vm"]
        vm_id.append(id)

# print(id)
if vm_id != []:
    for id in vm_id:
        s.post("https://172.17.41.44/rest/vcenter/vm/"+id+"/power/start")
else:
    print("All the VMs are in powered on State")

'''

'''
Enumarate - returning index as well as value

l = ['ankush','patekar','rahul','Ajay']
for ind, val in enumerate(l):
    print("Name " + val + " is listed at " , ind)
'''
'''
Unlike lists, items in dictionaries are unordered.
list:
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
if spam == bacon:
    print(True)
else:
    print(False)
    
Dict:
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

if eggs == ham:
    print(True)
else:
    print(False)

'''
'''
The join() Method
The join() method is useful when you have a list of strings that need to be joined together into a single string value.
The join() method is called on a string, gets passed a list of strings, and returns a string.
string = ' '.join(['My', 'name', 'is', 'Simon'])
-> My name is Simon
print(string)

split() Methods
called on a string value and returns a list of strings

x = ("Ankush_1234").split('_')
print(x)
['Ankush', '1234']
'''

'''
ord() and chr() Functions
print(ord("Z"))
print(chr(50))
'''


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = []
#
# for x in fruits:
#     if x == "banana":
#         x = "orange"
#     newlist.append(x)
#
# print(newlist)

# with open("test.txt", "r") as f:
#     print(f.read())

'''
# wite a function in Python to count and display the total number of words in a text file

def fword():
    with open("test.txt", "r") as f:
      data = f.read()
    # file = open("test.txt", "r")
    # data = file.read()
    print(data)
    words = data.split()
    count = 0
    for word in words:
        count = count + 1
    print(count)
fword()

'''


'''
# Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters

def display_words():
    with open("test.txt", "r") as f:
        data = f.read()
        print(data)
    words = data.split()
    for word in words:
        if len(word) < 4:
            print(word)
display_words()
'''

'''
# Write a function in Python to count words in a text file those are ending with alphabet "e"
def words_end_e():
    with open("test.txt", "r") as f:
        data = f.read()
        print(data)
        words = data.split()
        count_End_with_E = 0
        for word in words:
            if word.endswith('e'):
                count_End_with_E = count_End_with_E +1
        print(count_End_with_E)
words_end_e()
'''




