def shortestSubarray(A,K):
    if len(A) == 0:
        return -1
    sum = A[0]
    if (sum >= K):
        return 1
    for i in range(1, len(A)):
        sum += A[i]
        if sum >= K:
            return i+1
    return -1

if __name__ == "__main__":
    a = [17,85,93,-45,-21]
    k = 150
    print(shortestSubarray(a, k))