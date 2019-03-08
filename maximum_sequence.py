def maxSequence(arr):
    M = [0]*len(arr)
    M[0]=arr[0]
    for i in range(1, len(arr)):
        M[i]=max(arr[i], M[i-1]+arr[i])
    return max(M)

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))