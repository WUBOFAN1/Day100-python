def gongyueshu(x,y):
    if x<y:
        x,y=y,x
    while x%y!=0:
        r=x%y
        x=y
        y=r
    return y
def gongbeishu(x,y):
    return x*y//gongyueshu(x,y)
