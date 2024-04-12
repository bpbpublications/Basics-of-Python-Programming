class Course:
    __fees=0
    __course_name=""
    def __init__(self):
        self.__fees = 3000
        self.__course_name="Java"
    def getinfo(self):
        print('course fees is::' + str(self.__fees))
        print('course name is::' + str(self.__course_name))

#obj1 is the object of a class Course
obj1 = Course()
#function getinfo() is called using obj1
obj1.getinfo()
# These are private variables,therefore, cann't change it.
obj1.__fees=4000
obj1.__course_name="C++"
obj1.getinfo()



