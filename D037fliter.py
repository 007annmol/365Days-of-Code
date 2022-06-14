#program using fiter fun to retune only values that are even and others discarded
a=list(map(int,input().split()))
eve=list(filter(lambda n:n%2==0, a))
print(eve)