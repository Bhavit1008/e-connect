def theLoveLetterMystery(s):
    rev = s[::-1]
    n = len(s)
    c = []
    total = 0
    for i in range(n):
        total = total + abs(ord(rev[i]) - ord(s[i]))
        c.append(total)        
    return total//2
