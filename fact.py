def recursiveFact(a):
    if a==0:
        return 1
    else:
        return a*recursiveFact(a-1)