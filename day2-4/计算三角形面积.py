a=float(input("第一条边:"))
b=float(input("第二条边:"))
c=float(input("第三条边:"))
if a+b<c or a+c<b or b+c<a:
    print("Error!")
else:
    print("周长:%f"  % (a+b+c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))