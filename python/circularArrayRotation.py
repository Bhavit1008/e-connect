def circularArrayRotation(a, k, queries):
    res = []
    res = (a[-k:] + a[:-k])
    out = []
    l = len(a)
    for i in queries:
        if(i > l):
            return -1
    for i in queries:
        out.append(res[i])
    return out
