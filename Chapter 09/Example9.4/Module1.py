try: 
# import statement is used to import the module i.e. test
 import test
# function sub() is called and parameters are passed as 4,3
 d=test.sub(4,3)
 print ("The output is",d)
except ImportError as exc:
 print ("Module not exists")
