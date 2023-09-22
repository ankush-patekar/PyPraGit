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
