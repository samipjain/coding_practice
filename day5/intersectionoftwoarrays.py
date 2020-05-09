def intersection(nums1, nums2):
    result = []
    if len(nums1) < len(nums2):
        smallestArray = nums1
        largeArray = nums2
    else:
        smallestArray = nums2
        largeArray = nums1

    for i in smallestArray:
        if i in largeArray:
            if i not in result:
                result.append(i)
    return result
    
if __name__ == "__main__":
    nums1 = [2,6,2,9,1]
    nums2 = [7,1]
    print(intersection(nums1, nums2))