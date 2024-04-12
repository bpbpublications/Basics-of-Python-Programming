class Course:
    def __init__(self,course,duration):
        self.cname = course
        self.cduration = duration
    def Name(self):
        return self.cname + "" + self.cduration
class detail(Course):
    def __init__(self,course,duration,fees):
        Course.__init__(self,course,duration)
        self.cfees = fees
    def GetDetail(self):
        return self.Name() + ", " +  self.cfees
x = Course("C++", "4 weeks")
y = detail("PHP", "4 weeks", "4000")
print(x.Name())
print(y.GetDetail())



