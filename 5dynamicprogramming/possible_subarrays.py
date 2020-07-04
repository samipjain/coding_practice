def allSubarrays(nums):
    result = []
    nums_length = len(nums)
    max_sum = -9999
    for i in range(nums_length):
        for j in range(i+1, nums_length+1):
            max_sum = max(sum(nums[i:j]), max_sum)
            result.append(nums[i:j])
    return max_sum

if __name__ == "__main__":
    print(allSubarrays([2,1,-3,4,-1,2,1,-5,4]))