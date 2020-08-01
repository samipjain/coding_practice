'''
Given an array of ints, compute recursively the number of times that the value 11 appears in the array. 
We'll use the convention of considering only the part of the array that begins at the given index. In this
 way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0
'''

def array11(arr, index):
    if len(arr) == index:
        return 0
    if arr[index] == 11:
        return 1 + array11(arr, index+1)
    return array11(arr, index+1)

print(array11([1, 2, 11], 0))
print(array11([11, 11], 0))
print(array11([1, 2, 3, 4], 0))
print(array11([], 0))
print(array11([11, 2, 3, 4, 11], 2))
