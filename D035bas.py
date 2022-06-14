#to input a list i a single read
#this reads the input and store it in a as a list but in string format
a=input("enter value").split()
#if u want to store values as int or flot in list with single input use map()
b=list(map(int,input().split()))
print(a,b)

#to find square of values given in the list
sqnum=list(map(lambda n:n**2 ,b))
print(sqnum)