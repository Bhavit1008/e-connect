def pangrams(s):
    s = s.lower()
    a = set(s)
    if(len(a) == 27):
        return "pangram"
    else:
        return "not pangram"
