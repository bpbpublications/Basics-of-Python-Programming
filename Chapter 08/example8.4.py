import re
# Regular expression for checking only string value
exp= r'\b[A-Za-z]+\b'
fname = input("Enter Your Name")
if(re.findall(exp,fname)):
    print("Welcome:",fname)
else:
    print("Wrong Input,Enter only string value")


