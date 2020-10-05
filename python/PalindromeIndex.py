def palindromeIndex(s):
    rev = s[::-1]
    if(rev == s):
        return -1
    else:
        n = len(s)
        a = list(s)
        for i in range(len(a)//2):
            if a[i] != a[len(a)-1-i]:
                a.pop(i)
                if a == a[::-1]:
                    return i
                else:
                    return (len(a)-i)        
