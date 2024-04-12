def func_divide(var3,var4):
    assert var4!=0,"Exception of Division by zero"
    return var3/var4

var1 = int(input("Enter First Value"))
var2 = int(input("Enter Second Value"))
output = func_divide(var1,var2)
print(output)  

