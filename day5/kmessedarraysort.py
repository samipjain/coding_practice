'''
Given an array of integers arr where each element is at most k places away from its sorted position, 
code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, 
an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution
'''
def sort_k_messed_array(arr, k):
  for i in range(0, len(arr)-1):
    for j in range(1, k+1):
      if i+j < len(arr):
        if arr[i] > arr[i+j]:
            temp = arr[i]
            arr[i] = arr[i+j]
            arr[i+j] = temp
  return arr

if __name__ == "__main__":
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    print(sort_k_messed_array(arr, k))
    