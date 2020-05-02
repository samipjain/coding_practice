arr = [1, 4, 20, 3, 10, 5]
sum = 33
n = len(arr)
flag = False

for i in range(0, n):
    temp_sum = arr[i]

    j = i+1
    while j <= n:
        if temp_sum == sum:
            print("Sum found between")
            print("indexes %d and %d"%(i, j-1))
            flag = True
        if temp_sum > sum or j == n:
            break
        temp_sum = temp_sum + arr[j]
        j += 1

if flag == False:
    print("No subarray founf")