try:
   fo = open("C:\\test2.txt","w")
   fo.write("This is test file")
except IOError:
   print ("Error: enable to find file or read data")
else:
   print ("data written in the file successfully")

fo.close()





