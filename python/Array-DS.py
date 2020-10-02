def reverseArray(a):
    l = []
    for i in reversed(a):
        l.append(i)

    #by slicing
    #l = a[::-1]

    #by reverse()
    #l = a.reverse()
    return l
