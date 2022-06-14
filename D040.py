def eve(n):
    for i in n:
        if i%2==0:
            print(i,"is even number")
        else:
            print(i,"is odd number")

rng=int (input("Enter the rang:"))
eve(range(1,rng))