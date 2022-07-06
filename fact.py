def recursiveFact(a):
    if a==0:
        return 1
    else:
        return a*recursiveFact(a-1)

def iterativeFact(a):
    res=1
    for i in range(2,a+1):
        res*=i
    return res
