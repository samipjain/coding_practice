def searchinsert(nums, target):
    l=0
    r=len(nums)-1
    return binarySearch(nums, target, l, r)
    

def binarySearch(nums, target, l, r):
    middle = int((l+r)/2)
    if (l < r):
        if target > nums[middle]:
            return binarySearch(nums, target, middle+1, r)
        elif target < nums[middle]:
            return binarySearch(nums, target, l, middle)
        elif target == nums[middle]:
            return middle
    else:
        return None

if __name__ == "__main__":
    arr = [1,3,5,6]
    target = 0
    print(searchinsert(arr, target))