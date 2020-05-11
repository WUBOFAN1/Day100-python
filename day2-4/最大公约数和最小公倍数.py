a=int(input("第一个数:"))
b=int(input("第二个数:"))
m=a
n=b
if a<b:
    c=a
    b=c
    a=b
while(b!=0):
    r=a%b
    a=b
    b=r
print("最大公约数为%d" %a)
print("最小公倍数为%d" %(m*n/a))
