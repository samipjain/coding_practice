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

def moveZerosToEnd2(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

if __name__ == "__main__":
    arr = [6,1,0,3,0,-1,2]
    # Out [6,1,3,0,-1,2,0]
    # Out [6,1,3,-1,2,0,0]
    # Out [6,1,3,-1,2,0,0]
    # print(moveZerosToEnd(arr))
    print(moveZerosToEnd2(arr))