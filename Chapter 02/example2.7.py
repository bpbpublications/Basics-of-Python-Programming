n = 5  #variable is declared
result = 0 #variable is initialized to 0
i = n  # n value is passed to i
while(i!=0): #loop will iterate until i is not equal to 0
   result=result+n 
   print(str(i) + ' ' + 'loop value is' + ' ' + str(result))
   i=i-1 # i value will decrement one by one
   
print(str(n) + '*' + str(n) + '=' + str(result))
