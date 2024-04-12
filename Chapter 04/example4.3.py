# Here a list is defined
lst1=[7,8,9,10,11,12,15]
# Get every second element
output = lst1[::2]  
print(output)  # Output: [7,9,11,15]
# Get every third element
output = lst1[::3]  
print(output)  # Output: [7,10,15]
# In case of Strings
lst2= "Python Course"
# Start from 1st index in above given string
# and get every second character
output= lst2[1::2]
print(output)  # Output: yhnCus
# Reverse of a List1 using negative step size i.e.-1
output = lst1[::-1]
print(output)
# Reverse of a String using negative step
output = lst2[::-1]
print(output)
# Following the start,stop and step sequence for List
# Here, it means start from 0th index,
# 4th index is the stop i.e.slice end and
# 2 is the step size
lst3 = [10,11,12,15,25,27]
output = lst3[0:5:2]
print(output)


