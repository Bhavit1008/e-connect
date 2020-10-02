def hackerrankInString(s):
    msg = "hackerrank"
    if(len(s) < len(msg)):
        return "NO"
    else:
        j = 0
        for i in range(len(s)):
            if(s[i] == msg[j] and j<len(s)):
                j = j + 1
        if(j==len(msg)):
            return "YES"
        else:
            return "NO"
