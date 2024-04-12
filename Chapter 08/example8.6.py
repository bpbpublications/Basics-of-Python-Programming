import re
# function is defined here
def mobile_validate(mobileno):
# Regular Expression pattern for Mobile Number is defined     
    exp = r'^\d{10}$'
# Check the Mobile no.digits using re.match()
    if re.match(exp,mobileno):
        return True
    else:
        return False

mobileno=input("Enter Your Mobile Number")
if mobile_validate(mobileno):
    print(f"{mobileno} is a valid Mobile number.")
else:
    print(f"{mobileno} is not a valid Mobile number.")



