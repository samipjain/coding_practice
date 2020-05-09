def intersection(nums1, nums2):
    result = []
    for i in nums1:
        for j in nums2:
            if i == j:
                if i not in result:
                    result.append(i)

    return result

if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersection(nums1, nums2))