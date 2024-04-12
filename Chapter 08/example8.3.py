import re
def checkemail(emailid):
# regular expression pattern for a valid email address
    expression = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# Using re.match to check email pattern in the expression 
    if re.match(expression,emailid):
        return True
    else:
        return False
# Input email address
emailid = input("Input an email address:")
# Function checkemail() is called and emailid is passed as parameter
if checkemail(emailid):
    print(emailid, " ","is"," ","Valid")
else:
    print(emailid," ","is"," ","Invalid")



    
