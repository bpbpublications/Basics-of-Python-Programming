num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2:
    if num1>num3:
        print("The greatest number is num1:",num1)
    else:
        print("The greatest number is num3:",num3)
else:
    if num2>num3:
        print("The greatest number is num2:",num2)
    else:
        print("The greatest number is num3:",num3)
