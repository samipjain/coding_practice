'''

Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.


countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
'''

def counthi(a):
    print("str ", a)
    if a == '':
        return 0
    if a[0] == 'h':
        if len(a) != 1 and a[1] == 'i':
            return 1 + counthi(a[2:])
    return counthi(a[1:])
    
print(counthi('ihxhixhiasxhihi'))