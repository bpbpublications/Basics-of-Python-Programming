import sys
try:
   no = int(input("Enter a number"))
except ValueError:
   print("Enter only numbers")
   sys.exit()
print("you entered number",no)




