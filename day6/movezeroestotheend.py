def moveZerosToEnd(arr):
    i = 0
    j = len(arr) - 1
    while(j > i):
        if arr[j] == 0:
            j=j-1
        if arr[i] != 0:
            i=i+1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i=i+1
            j=j-1
    return arr

if __name__ == "__main__":
    arr = [6,1,0,3,0,-1,2]
    # Output [6,1,3,-1,2,0,0]
    # Actual [6, 1, 2, 3, -1, 0, 0]
    print(moveZerosToEnd(arr))