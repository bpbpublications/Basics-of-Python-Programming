n = int(input("Enter the Number"))  
i = int(n)
rev = 0

while(i>0):  #while loop will execute only if the condition is true
   rem=i%10  #remainder is obtained using % (modulus) operator
   rev=rev*10+rem  
   i = i//10


print("The reverse of a no.is",rev)

if(n==rev):
 print(str(n) + "is a palindrome number")
else:
 print(str(n) + "isn't a palindrome number")
 
