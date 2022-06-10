msum=0
for i in range (5,11,2):
    msum+=i
    if msum==5:
        continue
    msum+=1
    print(msum)