'''
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields 
the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
'''

def sumDigits(n):
    return sumDigitsUtil(n ,0)

def sumDigitsUtil(n, sum):
    print("n ", n, "sum ", sum)
    if n == 0:
        return sum
    sum += n%10
    digit = n//10
    return sumDigitsUtil(digit, sum)

print(sumDigits(23456))