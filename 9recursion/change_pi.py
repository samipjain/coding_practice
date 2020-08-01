'''
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".


changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
'''

def changePi(s):
    print("str ", s)
    if s == '':
        return ''
    if s[0] == 'p':
        if len(s) > 1 and s[1] == 'i':
            return '3.14' + changePi(s[2:])
    return s[0] + changePi(s[1:])

print(changePi("xpix"))
print(changePi("pipi"))
print(changePi("pip"))