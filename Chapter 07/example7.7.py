class Course:
    fees=0
    course_name=""
    def __init__(self):
        self.fees = 3000
        self.course_name="Java"
    def getinfo(self):
        print('course fees is::' + str(self.fees))
        print('course name is::' + str(self.course_name))

#obj1 is the object of a class Course
obj1 = Course()
#function getinfo() is called using obj1
obj1.getinfo()
# Now, these are public variables,therefore, we can change the values.
obj1.fees=4000
obj1.course_name="C++"
obj1.getinfo()



