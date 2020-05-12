num=1
for i in range(1,10001):
    total=0
    if i==1:
        print("第%d个完美数为%d"%(1,1))
        num+=1
    if i!=1 and i!=2:
        for j in range(1,int(i/2)+1):
            if i%j==0:
                total=total+j
        if total==i:
            print("第%d个完美数为%d"%(num,i))
            num+=1

