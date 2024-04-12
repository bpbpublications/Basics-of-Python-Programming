msg = input("Input a sentence:") 
cnt = {"digits":0, "lower":0, "upper":0,"vowels":0}
for char in msg: 
   if char.isdigit(): 
      cnt["digits"] = cnt["digits"]+1 
   elif char.isupper(): 
      cnt["upper"] = cnt["upper"]+1 
   elif char.islower(): 
      cnt["lower"] = cnt["lower"]+1

print("No.of Digits are:",cnt['digits'])
print("No.of Uppercase letters are:",cnt['upper'])
print("No. of Lowercase letters are:", cnt['lower'])
# Display the output
vowels = 'aeiouAEIOU'
for char in msg:
   if char in vowels:
      cnt["vowels"]=cnt["vowels"]+1
# Display the output
print("No.of Vowels are:", cnt['vowels'])


