'''

Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only 
the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. 
The initial call will pass in index as 0.


array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
'''

def array6(arr, index):
    print("arr ", arr, "index", index)
    if len(arr) == index:
        return False
    if arr[index] == 6:
        return True
    return array6(arr, index+1)

print(array6([1, 6, 4, 6], 0))
print(array6([1, 4], 0))
print(array6([6], 0))