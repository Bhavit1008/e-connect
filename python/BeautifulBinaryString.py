def beautifulBinaryString(b):
    c = 0
    for i in range(0,len(b)-2):
        if(b[i]=='0' and b[i+1]=='1' and b[i+2]=='0'):
            c = c + 1
    if(c ==0):
        return c
    else:
        return c-1
