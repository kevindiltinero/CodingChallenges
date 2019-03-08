def maxSequence(arr):
    if len(arr) == 0:
        return 0
    M = [0]*len(arr)
    M[0]=arr[0]
    for i in range(1, len(arr)):
        M[i]=max(arr[i], M[i-1]+arr[i])
    if max(M) < 0:
        return 0
    return max(M)