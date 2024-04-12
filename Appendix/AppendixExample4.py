class A:

    def __init__(self,fname,lname,sid):
        self.first=fname
        self.last=lname
        self.sno=sid
    def __str__(self):
        return self.first + " " + self.last + " " + self.sno

y = A("Sunil", "Kumar", "110")
print(y)


