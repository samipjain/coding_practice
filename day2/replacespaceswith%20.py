def replaceSpaces(s):
    s = s.replace(" ", "%20")
    print("Output1: ", s)

def replaceSpaces2(s):
    countSpaces = countOfChars(s)
    i = len(s)

    new_len = countSpaces * 2 + len(s)
    index = new_len - 1
    s = list(s)

    for j in range(i-2, new_len-2):
        s.append('0')

    for j in range(i-1, 0, -1):
        if(s[j] == " "):
            s[index] = "0"
            s[index-1] = "2"
            s[index-2] = "%"
            index = index-3
        else:
            s[index] = s[j]
            index -= 1
    print("".join(s))

def countOfChars(s):
    count = 0
    for i in range(len(s)):
        if(s[i] == " "):
            count += 1
    return count

s = "Mr John Smith    "
# output "Mr%20John%20Smith"
s = s.strip()
print(replaceSpaces(s))
print(replaceSpaces2(s))
