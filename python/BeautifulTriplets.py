def beautifulTriplets(d, arr):
    c = 0
    n = len(arr)
    for i in range(n):
        if((arr[i] + d) in arr and (arr[i] + 2*d) in arr):
            c += 1
    return c