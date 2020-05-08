def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    res = ""
    for ch in s:
        if ch != "]":
            stack.append(ch)
        else:
            temp = stack[-1]
            curr_ch = ""
            while(temp != "["):
                curr_ch = stack.pop() + curr_ch
                temp = stack[-1]
            remov_open_bracket = stack.pop()
            num = stack.pop()
            res += int(num) * curr_ch
    return res
        
if __name__ == "__main__":
    expr = "3[a]2[c]"
    print(decodeString(expr))