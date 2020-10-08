def acmTeam(topic):
    n = len(topic)
    count =0
    for i in range(0,n-1):
        for j in range(i+1,n):
            a = bin(int(topic[i],2) | int(topic[j],2)).count("1")
            if a > res:
                res = a
                count = 1
            elif (a == res):
                count +=1
    return res,count
