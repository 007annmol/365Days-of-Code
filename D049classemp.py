class Emp:
    def __init__(self,name,id):
        self.ename=name
        self.eid=id
    def display(self):
        print("ID:%d\nName:%s\n" %(self.eid,self.ename))

e1=Emp(input("enter e1 name:"),int(input("enter e1 id:")))
e2=Emp(input("enter e2 name:"),int(input("enter e2 id:")))

e1.display()
e2.display()
