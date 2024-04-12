import re
# Regular expression for checking only integer value
exp= r'\b[0-9]+\b'
rollno = input("Enter Your Rollno")
if(re.findall(exp,rollno)):
    print("Welcome:",rollno)
else:
    print("Wrong Input,Enter only integer value")


