def matchingStrings(strings, queries):
    s = 0
    l = []
    for i in queries:
        s=0
        for j in strings:
            if(i==j):
                s=s+1
        l.append(s)
    return l
