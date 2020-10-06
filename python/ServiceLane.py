def serviceLane(n, cases):
    print(cases)
    l = []
    res = []
    #[[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
    for i in cases:
        l = []
        for j in range(i[0],i[1]+1):
            print(j)
            l.append(width[j])
        print(l)
        print("change")
        m = min(l)
        res.append(m)
    return res
