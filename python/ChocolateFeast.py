def chocolateFeast(n, c, m):
    choco = n//c
    rem = choco//m
    total = choco + (choco -1)//(m-1)
    return total
