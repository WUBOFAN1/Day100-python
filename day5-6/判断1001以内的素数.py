num=0
for i in range(1,101):
    if i==1:
        continue
    j=2
    while i%j!=0:
        j+=1
    if j==i:
        num+=1
        print("第%d个素数是%d"%(num,j))