def isValid(s):
    count_0 = 0
    count_1 = 0
    # print("inside", s)
    for char in s:
        if char == '0':
            count_0 += 1
        elif char == '1':
            count_1 += 1
    if count_0 != count_1:
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
                print(s[i:j])
                count += 1
    return count

if __name__ == "__main__":
    print(countBinarySubstrings('00110'))
    # print(countBinarySubstrings('00110011'))
    # print(countBinarySubstrings('10101'))