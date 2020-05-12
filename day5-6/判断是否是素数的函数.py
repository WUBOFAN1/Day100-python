def sushu(num):
    p=2
    while num%p!=0:
        p+=1
    if(p==num):
        return True
    else:
        return False
