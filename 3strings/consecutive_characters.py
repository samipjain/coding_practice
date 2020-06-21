def maxPower(s):
    """
    :type s: str
    :rtype: int
    """
    prev_char = s[0]
    result = []
    temp_result = 1
    
    for char in s[1:]:
        if char == prev_char:
            temp_result += 1
        else:
            prev_char = char
            result.append(temp_result)
            temp_result = 1
    result.append(temp_result)
            
    return 1 if len(result) == 0 else max(result)

if __name__ == "__main__":
    print(maxPower('leetcode'))
    print(maxPower('abbcccddddeeeeedcba'))
    print(maxPower('a'))
    print(maxPower('aa'))
    print(maxPower('bbaaa'))