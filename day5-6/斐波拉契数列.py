num=int(input("输出前n个数字："))
value_1=1
value_2=1
print("第1个数为%d"%value_1)
print("第2个数为%d"%value_2)
for i in range (num-2):
    total=value_1+value_2
    print("第%d个数为%d"%(i+3,total))
    value_1=value_2
    value_2=total
    i+=1

