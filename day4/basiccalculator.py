'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
Input: " 2-1 + 2 "
Output: 3
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
                
            elif ch == "+":
                res += sign * operand

                sign = 1
                operand = 0
        
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            
            elif ch == ")":
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign * operand


if __name__ == "__main__":
    s = Solution()
    expr = "(7-8+9)"
    print(s.calculate(expr))