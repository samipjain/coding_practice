NO_OF_CHARS = 256

def isPermutationOfPalindrome(s):
    print(s)
    count = [0] * NO_OF_CHARS

    for i in range(0, len(s)):
        count[ord(s[i])] = count[ord(s[i])] + 1
    
    odd = 0
    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            print(i)
            print(count[i])
            odd = odd + 1
        if (odd > 1):
            return False
    return True

string = "Tact Coa"
string = string.lower()
string = string.strip()
string = string.replace(" ", "")
print(isPermutationOfPalindrome(string))