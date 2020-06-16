"""
    A=[1,2,0,0], K = 34
    Output = [1,2,3,4]
    Explanation: 1200 + 34 = 1234
"""

def addToArrayForm1(A, K):
    # Calculate the size of array
        l = len(A) - 1
        
        # Convert array into a number
        # i = 0, sum = 0 + A[0] * (10**3) = 0 + 1*1000 = 1000
        # i = 1, sum = 1000 + A[1] * (10**2) = 1000 + 2*100 = 1200
        # i = 2, sum = 1200 + A[2] * (10**1) = 1200 + 3*10 = 1230
        # i = 3, sum = 1230 + A[3] * (10**0) = 1230 + 4*1 = 1234
        sum = 0
        for i in range(0, len(A)):
            sum = sum + A[i] * (10**l)
            l = l-1

        return [int(char) for char in str(sum + K)]

def addToArrayForm2(A, K):
        A_str = ''
        for e in A:
            A_str = A_str + str(e)

        return [int(char) for char in str(int(A_str) + K)]

if __name__ == "__main__":
    print(addToArrayForm1([1,2,0,0], 34))
    print(addToArrayForm2([2,1,5], 806))