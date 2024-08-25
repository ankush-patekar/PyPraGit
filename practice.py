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
        # print(data)
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

'''
# Write a program to enter names of employees and their salaries as input and store them in a dictionary
count = 0
d = {}
while count <= 4:
    name = input("Enter name: ")
    salary = input("Enter salary")

    d[name] = salary
    count = count +1
print(d)
'''

'''
# Write a program that reads string from user. Your program should create a dictionary having key as word length and value is count of words of that length.

s = input("Enter string: ")
d = {}
for word in s.split():
    if len(word) in d:
        d[len(word)] += 1
    else:
        d[len(word)] = 1
print(d)
# '''
#         ************************ String  *******************************

''''
# Write a Python program to count the number of vowels and consonants in a given string.

string = input("Enter any string: ")
# string = 'Anushka'
v = []
c = []
vcount=0
for s in string:
    if s == 'a' or s=='e' or s=='i 'or s=='o' or s=='u' or s=='A' or s=='E' or s=='I' or s=='O' or s=='U':
        v.append(s)
        vcount= vcount+1
    else:
        c.append(s)

print("Vowels in given String: ", v)
print("number of vowels in given string: ", vcount)
# print(c)
'''

'''
# Write a Python program to check if a string entered by the user is a palindrome or not

str1 = input("ENter any string: ")

if str1 == str1[::-1]:
    print("Entered string is palindrome")
else:
    print("Not Palindrome")
'''
'''
# Write a Python program to perform basic string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string is not smaller than the original string, your method should return the original string.

def com_str(s):
    com_str = ''
    ctr = 1
    for i in range(1, len(s)+1):
        if s[i]==s[i-1]:
            ctr+=1
        else:
            com_str = com_str + s[i-1] + str(ctr)
            ctr = 1
    return com_str if len(com_str) < len(s) else s

com_str('abbccc')
print(com_str())
'''

'''
# Word Frequency: Write a Python program that takes a string as input and calculates the frequency of each word in the string. Output the words and their corresponding frequencies.
# Character Frequency: Write a Python program that takes a string as input and calculates the frequency of each character in the string. Output the characters and their corresponding frequencies
test_string = 'Jaudyanagade'
d={}
# for c in test_string.split():           to calculate frequency of words
for c in test_string:                    To calculate frequency of char
    if c not in d:
        d[c]=1
    else:
        d[c] += 1
print(d)
'''

'''
# Write a Python program to determine if a string has all unique characters. Return True if the string has all unique characters, and False otherwise.

test_string = input("Enter string: ")
list = []
for c in test_string:
    if c not in list:
        list.append(c)
    else:
        pass
if len(list) <= 1:
    print(True)
else:
    print(False)

'''

'''
# Word Reversal:
# Write a Python program that takes a sentence as input and reverses the order of words in the sentence. For example, if the input is "Hello World," the output should be "World Hello."

test_string = input("Enter string: ")
# test_string = 'hello world'
words = test_string.split()

rev_string = " ".join(reversed(words))
print(rev_string)
'''

'''
# Title Case Conversion:Write a Python program that converts a given sentence to title case. Title case means that the first letter of each word in the sentence is capitalized, and all other letters are in lowercase.

test_string = 'i love my india'
print(test_string.title())

'''

'''
# Substring Removal:Write a Python function that removes all occurrences of a specified substring from a given string. The function should take two strings as input: the main string and the substring to be removed


def remove_SubString(mstr, sstring):
    l1 = []
    for c in mstr:
        l1.append(c)

    for c in sstring:
        if c in l1:
            l1.remove(c)

    print("".join(l1))

remove_SubString('ankush', 'auz')
'''

# *************************************** List ****************************************

'''
List Manipulation:
Write a Python program to perform the following operations on a list:

Add an element to the end of the list
Insert an element at a specific position
Remove an element from the list by value
Sort the list in ascending and descending order


test_list = [1,2,4,7 , 55, 'ankush', '23.5']

test_list.append('end')
print(test_list)
test_list.insert(2, 'insert')
print(test_list)
test_list.remove(1)
print(test_list)
test_list.sort()

'''

'''
# List Reversal:Write a Python program to reverse a list without using the reverse() method.

# test_list = [5,6,7,8,9]
# rev_list = test_list[::-1]

original_list = [1, 2, 3, 4, 5]
print("List before reverse : ",original_list)
reversed_list = []
for value in original_list:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)
'''


'''
#List Intersection: Write a Python program to find the intersection of two lists. Intersection means the elements common to both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 1]
list3 = []
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print(list3)

'''

'''
# List Rotation:
# Write a Python function that rotates a list by a specified number of positions. For example, if the input list is [1, 2, 3, 4, 5] and the rotation is 2, the output should be [3, 4, 5, 1, 2].

def rotate_list(lst, position):

    # Perform the rotation using list slicing
    rotated_list = lst[position:] + lst[:position]
    return rotated_list
lst = [1,2,3,4,5]
position = 5
print(rotate_list(lst, position))
'''
'''
# find min and max in list

lst = [1,2,3,4,5,9,8,6]
min_num= 0
max_num = 0
for n in lst:
    # min_num = n
    # max_num = n
    if n < min_num:
        min_num = n
    elif n > max_num:
        max_num = n
'''
# del, Pop and remove
'''
# Use del when you want to delete an element or slice by index.
# Use pop() when you want to remove and retrieve an element by index.
# Use remove() when you want to remove the first occurrence of a specific value from the list.

lst = [1,3,5,7,3,9]
del lst[2]
print(lst)

pop_ele = lst.pop(2)
print(pop_ele)

lst.remove(3)
print(lst)

'''
# decorator
'''
def my_decorator(fucn):
    def wrapper():
        print("before calling fn")
        fucn()
        print("after calling fn")
    return wrapper()

@my_decorator
def say_hello():
    print("Hello")

say_hello()
'''
# check given number is prime or not

num = int(input("enter any integer: "))
flag = False
if num < 2:
    print(num, "is prime")
else:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
if flag:
    print(num, "is not prime")
else:
    print(num, "is prime")