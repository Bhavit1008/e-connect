def equalizeArray(arr):
    m = [arr.count(i) for i in arr]
    c = len(arr) - max(m)
    print(m)
    return c
