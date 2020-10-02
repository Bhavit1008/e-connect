def marsExploration(s):
    l = len(s)
    no = l//3
    msg=""
    for i in range(no):
        msg = "SOS" + msg
    print(msg)

    c = 0

    for i in range(l):
        if(s[i] != msg[i]):
            c = c + 1
    return c
