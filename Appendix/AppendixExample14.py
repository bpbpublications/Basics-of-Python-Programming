a = [12,1,3,23,5]
x = 0
print("Array elements before sorting")
for i in range(0,5):
   print(a[i])
for i in range(0,5):
   for j in range(i+1,5):
#Element at the 0th position is compared with the 1st element and so on.       
      if(a[i]>a[j]):
       x=a[i]
       a[i]=a[j]
       a[j]=x
print("Elements after Sorting")
for i in range(0,5):
  print(a[i])


