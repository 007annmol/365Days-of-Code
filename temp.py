f=open("num.txt","r")
g=open("duplicate.txt","w")
for i in range(1,100):
    n=f.readline()
    m=f.read()
    for i in m:
        if(i==m):
            p