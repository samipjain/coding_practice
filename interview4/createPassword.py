''' 
Given two strings, create a password
str1 = 'abc' str2 = 'def'
output = 'adbecf

str1 = 'abc' str2 = 'defgh'
output = 'adbecfgh
'''

def createPassword(a, b):
    small_len = len(a) if len(a) < len(b) else len(b)
    result = ''

    for i in range(small_len):
        result += a[i]
        result += b[i]

    if len(a) < len(b):
        result += b[i+1:]
    else:
        result += a[i+1:]
    return result

if __name__ == "__main__":
    print(createPassword('abcopiu','defgg'))