def stringcompression(s):
    str1 = ""
    i = 0
    while (i <= len(s)-1):
        count = 1
        ch = s[i]
        j = i
        while(j < len(s)-1):
            if (s[j] == s[j+1]):
                j = j+1
                count = count + 1
            else:
                break
        str1 = str1 + ch + str(count)
        i = j+1
    print(str1)

string = "aaaab"

stringcompression(string)