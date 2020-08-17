'''
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given
 target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately 
 following it in the array must not be chosen. (No loops needed.)


groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false
'''

def groupNoAdj(start, nums, target):
    # print("start ", start, "nums ", nums, "target ", target)
    # if target == 0:
    #     return True
    # elif start >= len(nums):
    #     return False
    if start >= len(nums):
        return target==0
    else:
        return groupNoAdj(start+1, nums, target) or groupNoAdj(start+2, nums, target-nums[start])

print(groupNoAdj(0, [2, 5, 10, 4], 12))
print(groupNoAdj(0, [2, 5, 10, 4], 14))
print(groupNoAdj(0, [2, 5, 10, 4], 7))