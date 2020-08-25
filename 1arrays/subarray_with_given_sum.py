def givenSum(arr, sum):
    if len(arr) == 0:
        print("None")
    
    for i in range(0, len(arr)):
        total = 0
        for j in range(i, len(arr)):
            if total < sum:
                total += arr[j]
            else:
                break
        if total == sum:
            break
    
    if total == sum:
        print(i+1, " ", j)
    else:
        print(-1)

if __name__ == "__main__":
    givenSum([1,2,3,7,5], 12)
    givenSum([1,2,3,4,5,6,7,8,9,10], 15)
    givenSum([1,2,3,7,5], 76)