import re
str1 = "The destination is A!"
find = re.search("destination is .*(A|B|C|D)",str1)
if find: 
	print(find.group())
else:
	print("Unable to search")



