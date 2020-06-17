"""
Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
"""

def prefixesDivBy5(A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    answer = [False for i in A]
    result = ''
    
    # Iterate over A
    for i in range(len(A)):
        # For every i, find the binary number starting from index 0 to i
        result = result + str(A[i])
        base10 = int(result, 2)
        # If divide by 5 then true, else i++
        if base10 % 5 == 0:
            answer[i] = True
    return answer

if __name__ == "__main__":
    print(prefixesDivBy5([0,1,1]))