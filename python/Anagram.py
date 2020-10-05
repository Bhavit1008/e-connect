def anagram(s):
    n = len(s)
    if(n%2!=0):
        return -1
    else:
        count = 0
        s1, s2 = Counter(s[:n//2]), Counter(s[n//2:])
        for char in s2:
            print(char)
            current = s2[char] - s1.get(char,0)
            if current > 0:
                count += current
        return count
