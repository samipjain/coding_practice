def searchinsert(nums, target):
    for i in range(len(nums)):
        if(nums[i]==target):
            return i
    for j in range(len(nums)):
        if(target<nums[j]):
            return j
        
    return len(nums)

if __name__ == "__main__":
    arr = [1,3,5,6]
    target = 7
    print(searchinsert(arr, target))