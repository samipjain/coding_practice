'''
Given a string, compute recursively a new string where all the 'x' chars have been removed.


noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
'''

def noX(s):
    if s == '':
        return ''
    if s[0] == 'x':
        return ''+noX(s[1:])
    return s[0]+noX(s[1:])

print(noX("xaxbxa"))
print(noX("abc"))
print(noX("xx"))