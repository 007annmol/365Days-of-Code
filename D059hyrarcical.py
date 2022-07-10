from msilib.schema import Class


class School:
    def __init__(self,name) :
        self.name=name
    def GetName(self):
        print(self.name)
    
class Std1(School):
    def st1(self):
        print("Student 01")
    
class std2(School):
    def st2(self):
        print("Student 02")

s=Std1("Ann")
s.st1()
s.GetName()

t=std2("Steve")
t.st2()
t.GetName()