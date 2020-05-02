def checkPermutation(str1, str2):
    if (len(str1) != len(str2)):
        return False
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)

    for i in range(len(str1_sorted)):
        if (str1_sorted[i] != str2_sorted[i]):
            return False
    return True

str1 = "abcd"
str2 = "dabe"

if(checkPermutation(str1, str2)):
    print("Yes")
else:
    print("No")