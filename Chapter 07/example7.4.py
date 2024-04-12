class course():
	def __init__(self,duration,fees):
		self.duration = duration
		self.fees = fees
	def getTotal(self):
		print(self.duration,"is the duration and",self.fees,"is the fees of course")
class fees(course):
	def __init__(self,name):
		self.name = name	
	def getTotal(self):
		print(self.name," is the name of course")
f = fees("java")
c = course("4 weeks",4000)
f.getTotal()
c.getTotal()





