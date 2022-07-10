class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def GetName(self):
        print(self.name)
    def GetAge(self):
        print(self.age)

class Student:
    def __init__(self,rollno) :
        self.rollno=rollno
    def GetRollno(self):
        print(self.rollno)

class Resident(Person,Student):
    def __init__(self, name, age,rollno):
        Person.__init__(self,name,age)
        Student.__init__(self,rollno)

r= Resident("Roshan",21,105)
r.GetName()
r.GetRollno()
r.GetAge()