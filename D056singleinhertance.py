class Person:
    def __init__(self,name) :
        self.name=name
    def GetName(self):
        return self.name
    def isEmployee(self):
        return False

class Emp(Person):
    def isEmployee(self):
        return True

p=Person("Ann")
print(p.GetName(),p.isEmployee())

e=Emp("steve")
print(e.GetName(),e.isEmployee())