total = 0;               #Global variable is declared

global(total)
def sum(arg1,arg2):      #function sum() is defined here
   total = arg1 + arg2;  #local variable is declared
   print("Inside the function local total :",total)
   return total;
sum(10,20);	#function is called
print ("Outside the function global total :",total)




