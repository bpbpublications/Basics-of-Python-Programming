def fact(x):

	if x == 1:
	    return 1
	else: 
	    return (x * fact(x-1))

x = int(input("Enter the value"))
#Here fact(x) function is called
print("The factorial of", x, "is", fact(x))




