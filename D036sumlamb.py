a=list(map(int,input("Enter value:").split()))
b=list(map(int,input("Enter value:").split()))
sum=map( lambda n1,n2:n1+n2, a,b)
print(list(sum))