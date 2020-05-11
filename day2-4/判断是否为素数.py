value=int(input("输入一个数："));
n=2
while(value%n!=0):
    n+=1
if n==value:
    print("%d 是素数！"%value)
else:
    print("%d 不是素数!"%value)