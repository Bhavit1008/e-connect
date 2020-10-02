def rotateLeft(d, arr):
    # Write your code here
    a = arr[d:] + arr[0:d]
    return a