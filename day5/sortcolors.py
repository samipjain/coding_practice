def sortColors(nums):
    result=[0,0,0]
    arr = []
    for i in nums:
        result[i] += 1
    
    for i in range(0, result[0]):
        arr.append(0)
    for i in range(0, result[1]):
        arr.append(1)
    for i in range(0, result[2]):
        arr.append(2)
    return arr

if __name__ == "__main__":
    print(sortColors([2,0,2,1,1,0]))