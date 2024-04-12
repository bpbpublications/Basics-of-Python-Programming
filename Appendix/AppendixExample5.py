class A:
#On creating objects of respective class,values are passed here __init__()
    def __init__(self,fname,lname):
        self.first = fname
        self.last = lname
# Function 'Fullname()' is defined here
    def Fullname(self):
        return self.first + "" + self.last
# class B is inheriting class A
class B(A):
    def __init__(self,fname,lname,sid):
# the class 'A' variables are inherited in class B
        A.__init__(self,fname,lname)      
        self.sno = sid
# Function GetDetail() is defined here
    def GetDetail(self):
        return self.Fullname() + "," + self.sno
#Object x and y are created of class A and B
x = A("Sunil","Kumar")
y = B("Anil","Kumar","429")
#Functions are called using object x and y
print(x.Fullname())
print(y.GetDetail())


