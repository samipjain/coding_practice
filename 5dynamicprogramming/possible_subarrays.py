def allSubarrays(nums):
    result = []
    nums_length = len(nums)
    max_sum = -9999
    for i in range(nums_length):
        for j in range(i+1, nums_length+1):
            max_sum = max(sum(nums[i:j]), max_sum)
            result.append(nums[i:j])
    return max_sum

def allSubarraysDP(nums):
    result = []
    result.append(nums[0])
    
    for i in range(1, len(nums)):
        result.append(max(nums[i], nums[i]+result[-1]))
    return max(result)

if __name__ == "__main__":
    # print(allSubarraysDP([-2,1,-3,4,-1,2,1,-5,4]))
    print(allSubarraysDP([-1,4,-3,5]))