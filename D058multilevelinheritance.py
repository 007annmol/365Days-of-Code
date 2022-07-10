from msilib.schema import Class


class First:
    def first(self):
        print("First Class")

class Second(First):
    def sec(self):
        print("Second class")

class Third(Second):
    def third(self):
        print("Third Class")

t=Third()
t.third()
t.first()
t.sec()