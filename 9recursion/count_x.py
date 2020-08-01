'''
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
'''

def countx(a):
    print("str ", a)
    if a == '':
        return 0
    if a[0] == 'x':
        return 1 + countx(a[1:])
    else:
        return countx(a[1:])

print(countx('xhixhixasx'))