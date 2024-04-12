var1 = 25  # This is a global variable

def global_fun():
# This allows to modify the global variable 'var1' within the function
    global var1  
    var1 = var1 + 5
    print(var1)

#function is called here
global_fun()  # Output: 30
# Output: 30, as the global variable 'var1' has been modified within the function
print(var1)  

