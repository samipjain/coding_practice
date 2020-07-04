def binarysearch(nums, l, h, target):
    if h > l:
        m = int((l + h)/2)
        if target < nums[m]:
            return binarysearch(nums, l, m, target)    
        elif target > nums[m]:
            return binarysearch(nums, m+1, h, target)
        else:
            return m
    else:
        return -1
    
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return binarysearch(nums, 0, len(nums)-1, target)
   
if __name__ == "__main__":
    print(search([-1,0,3,5,9,12], 2))