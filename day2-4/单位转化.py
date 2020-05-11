unit=input("输入的单位:");
value=float(input("输入的长度:"));
if unit=="英寸":
    print("%f 英寸 等于 %f 厘米" %(value,value*2.54));
else:
    print("%f 厘米 等于 %f 英寸" %(value,value/2.54));