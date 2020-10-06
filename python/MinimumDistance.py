def minimumDistances(a):
    l = []
    n = len(a)
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i] == a[j]):
                l.append(abs(i-j))
    print(l)
    if(len(l)==0):
        return -1
    else:
        return min(l)
