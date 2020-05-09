def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    # stack = []
    # res = ""
    # for ch in s:
    #     if ch != "]":
    #         stack.append(ch)
    #     else:
    #         temp = stack[-1]
    #         curr_ch = ""
    #         while(temp != "["):
    #             curr_ch = stack.pop() + curr_ch
    #             temp = stack[-1]
    #         remov_open_bracket = stack.pop()
    #         num = stack.pop()
    #         res += int(num) * curr_ch
        
    #     if stack:
    #         for i in res:
    #             stack.append(i)
    #         res = ""
    # return res
    
    result = ""
    tempNum = ""
    num_stack = []
    string_stack = []

    for ch in s:
        if ch.isdigit():
            tempNum = tempNum + ch
        elif ch == "[":
            num_stack.append(int(tempNum))
            tempNum = ""

            string_stack.append(result)
            result = ""
        elif ch == "]":
            result = string_stack.pop() + result * num_stack.pop()
        else:
            result +=  ch
    return result
        

if __name__ == "__main__":
    expr = "3[a]"
    print(decodeString(expr))