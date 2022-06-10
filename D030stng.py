from posixpath import split


s=input("enter a string: ")
print(s.upper())
print(s.strip())
print(s.replace('A','Z'))
print(s.split())
print("length=",s.__len__())