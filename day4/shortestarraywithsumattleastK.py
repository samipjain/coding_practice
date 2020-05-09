def shortestSubarray(A,K):
    if (len(A) == 1):
        return 1
    min_len = len(A)+1
    curr_sum = 0
    
    start, end = 0,0
    while(end < len(A)):
        while(curr_sum < K and end < len(A)):
            if (curr_sum <= 0 and K > 0):
                start = end
                curr_sum = 0
            curr_sum += A[end]
            end += 1

        while(curr_sum > K and start < len(A)):
            if (end - start < min_len):
                min_len = end - start
            curr_sum -= A[start]
            start += 1
    if min_len == len(A) + 1:
        return -1
    return min_len


if __name__ == "__main__":
    a = [2,-1,2]
    k = 3
    print(shortestSubarray(a, k))