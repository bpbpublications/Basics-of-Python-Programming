class course():
  def __init__(self):
      self.value = 5000
  def getdata(self):
      print(self.value, "is the fees of course")

class fees(course):
# getdata() function is defined here
  def getdata(self):
      self.value += 2000
      print(self.value, "is the increased fees of course")

# c is the object of the fees class
c = fees()
# getdata() is the function called by the c object 
c.getdata()



