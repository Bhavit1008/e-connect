def funnyString(s):
    l = []
    for i in s:
        c = ord(i)
        l.append(c)
    print(l)
    d = []
    d_rev = []
    for i in range(len(l)-1):
        d.append(abs(l[i]-l[i+1]))
    print(d)
    rev = l[::-1]
    for i in range(len(rev)-1):
        d_rev.append(abs(rev[i]-rev[i+1]))
    print(d_rev)
    print(rev)
    if(d == d_rev):
        return "Funny"
    else:
        return "Not Funny"
