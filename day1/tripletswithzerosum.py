def findTriplets(arr, arr_len):
    flag = False
    for i in range(0, arr_len-2):
        for j in range(i+1, arr_len-1):
            for k in range(j+1, arr_len):
                if ((arr[i] + arr[j] + arr[k]) == 0):
                    print(arr[i], arr[j], arr[k])
                    flag = True
    if(flag == False):
        print("No triplets")

def findTriplets2(arr, n):
    flag = False
    for i in range(0, n-1):
        s = set()
        for j in range(i+1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                flag = True
            else:
                s.add(arr[j])
        print(s)
    if(flag == False):
        print("No Triplets")

arr = [0, -1,2,-3,1]
arr_len = len(arr)

print("Method 1: O(n3)")
findTriplets(arr, arr_len)

print("Method 2: O(n2)")
findTriplets2(arr, arr_len)
