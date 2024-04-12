def menu():
    print("your options are:")
    print("")
    print ("1 Addition")
    print ("2 Subtraction")
    print ("3 Multiplication")
    print ("4 Division")
    print ("5 Quit")
    print (" ")
    return input("Choose your option:")
# this adds two numbers given
def add(a,b):		#  add()  function is defined
    print(int(a), "+", int(b), "=", int(a)+int(b))
# this subtracts two numbers given
def sub(a,b):		# sub() function is defined
    print (int(a), "-", int(b), "=", int(a) - int(b))
# this multiplies two numbers given
def mul(a,b):		# mul() function is defined
    print (int(a), "*", int(b), "=", int(a) * int(b))
# this divides two numbers given
def div(a,b):		# div() function is defined
    print (int(a), "/", int(b), "=", int(a) / int(b))

loop = 1
choice = 0
while loop==1:
    choice=menu()	# menu() function is called here
    if choice=='1':
        # inputs from user are passed as parameter in function
        add(input("Add this: "),input("to this: "))
    elif choice=='2':
        sub(input("Subtract this: "),input("from this: "))
    elif choice=='3':
        mul(input("Multiply this: "),input("by this: "))
    elif choice=='4':
        div(input("Divide this: "),input("by this: "))
    elif choice=='5':
        loop = 0
print ("Thankyou !")
