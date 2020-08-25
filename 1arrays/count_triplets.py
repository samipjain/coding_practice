def countTriplets(arr):
    if len(arr) == 0:
        return
    count = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) in arr:
                count += 1
    return count

if __name__ == "__main__":
    print(countTriplets([1,5,3,2]))
    print(countTriplets([3,2,7]))
    print(countTriplets([-3,2,-1, -4, 1]))