def isValid(s):
    prev = s[0]
    i = 0
    
    count_0 = 0
    count_1 = 0
    if prev == '0':
        count_0 += 1
    else:
        count_1 += 1

    for char in s[1:]:
        if char != prev:
            prev = char
            i += 1
        # dict_s[char] += 1
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1
    if count_0 != count_1:
        return False
    if i != 1:
        return False
    return True
    
def countBinarySubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isValid(s[i:j]):
                # print(s[i:j])
                count += 1
    return count

if __name__ == "__main__":
    print(countBinarySubstrings('00110'))
    print(countBinarySubstrings('00110011'))
    print(countBinarySubstrings('10101'))