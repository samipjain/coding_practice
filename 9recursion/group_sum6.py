'''

Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, 
such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. 
(No loops needed.)


groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
'''

def groupSum6(start, nums, target):
    # Check start index, if 6 pick thee value
    if start == len(nums):
        if target == 0:
            return True
        else:
            return False
    else:
        if nums[start] == 6:
            return groupSum6(start+1, nums, target-nums[start])
        else: 
            return groupSum6(start+1, nums, target) or groupSum6(start+1, nums, target-nums[start])

print(groupSum6(0, [5, 6, 2], 8))
print(groupSum6(0, [5, 6, 2], 9))
print(groupSum6(0, [5, 6, 2], 7))