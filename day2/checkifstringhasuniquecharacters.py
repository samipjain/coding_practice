def uniqueCharacters(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True

s = "absc10gd"

if uniqueCharacters(s):
    print("Unique")
else:
    print("Not unique")