var1 = int(input("Enter a number to check"))
# length of a input number is obtained
var2 = len(str(var1))
# Initialize result variable to 0
result = 0
# Temporary variable to store the original number
temp = var1
# while loop to calculate the sum of digits
while temp > 0:
	var3 = temp%10
	result = result + var3**var2
	temp = temp//10
# Check if the result variable is equal to the original number
if var1==result:
    print(f"{var1} is an Armstrong number.")
else:
    print(f"{var1} is not an Armstrong number.")

