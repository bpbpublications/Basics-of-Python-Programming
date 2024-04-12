# Logical AND
# Returns True if both conditions are True
age = int(input("Enter your age"))
citizen = "India"
if age>=18 and citizen=="India":
    print('Yes, you are eligible for vote')
else:
    print('No,you are not eligible for vote')
# Logical OR
# Returns True if atleast one condition is True
income = int(input("Enter your income"))
if age>=18 or income>25000:
    print('Yes,you are eligible for taking Loan')
else:
    print('No,you are not eligible for taking loan')



