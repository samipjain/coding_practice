# convert to lower case
# remove punctuations
# split
# create a dict
# check for each word in an array, if this word exist then increment the count, else insert a key-value pair

from heapq import heappush, heappop

def find_largest(arr, m):
    if arr is None or len(arr) is 0: 
        return 

    sorted_arr = sorted(arr, reverse=True)
    output = []

    for i in range(m):
        output.append(sorted_arr[i])
    return output

def find_largest_using_heap(input, m):
    max_nums = [float('-inf')]

    for i in input:
        if int(i) > max_nums[0]:
            if len(max_nums) >= m:
                heappop(max_nums)
            heappush(max_nums, int(i))

    return max_nums

if __name__ == "__main__":
    arr = [1,5,4,3,2,6]
    m = 3
    print(find_largest_using_heap(arr, m))