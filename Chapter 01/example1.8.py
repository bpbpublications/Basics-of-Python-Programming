#Logical and Bitwise operators in Python
a=1
b=0
#"and" operator will check both the conditions i.e.if one condition is true and another is false,then output will be false.
print(a and b)#output will be printed 0 i.e.false
#In "or" operator,one condition is true and another is false,then output will be true.
print(a or b) #output will be printed 1 i.e.true
print(not a)  #output will be "False"
c=int(input("Enter the value"))
print("The value of c is",c)
d=int(input("Enter the value"))
print("The value of d is",d)
#Bitwise And(&)operator
print('Result after Bitwise AND operation is',c&d)
#Bitwise or(|) operator
print('Result after Bitwise OR operation is',c|d)
#Bitwise XOR operator
print('Result after Bitwise XOR operation is',c^d)
#Bitwise Right Shift operator
print('Result after Right Shift operation is',c>>1)
#Bitwise Left Shift Operator
print('Result after Left Shift operation is',c<<1)
#Assignment operator
c+=10
print('c value after adding 10 using Assignment operator is',c)
c-=3
print('c value after subtracting 3 using Assignment operator is',c)
