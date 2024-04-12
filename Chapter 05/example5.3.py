course = {}  
course["Java"]="Used in Mobile Applications"
course["DotNet"]="For Web Based Applications"
course["1"]="php an open source for web applications"
course["2"]="Android for Mobile Computing"
# Value can be added to a numeric key also 
course[3]="Python is an interpreter-based"

print(course)	#print complete dictionary in key-value pairs form
print(course["1"])
course["Python"] = "Machine Learning" 	#add new dictionary key-value pair
del course["Java"]   	# delete this key-value pair
print(course["DotNet"])
print(course[3])#retrieving the value to a numeric key












