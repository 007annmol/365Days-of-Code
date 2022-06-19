class Student:
    """"class representing student"""
    def __init__(self,n,a) :
        self.fullname=n
        self.age=a
    
    def getage(self):
        return self.age