# Method 1 O(n2)
def uniqueCharacters(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True

# Method 2 O(nlogn)
def uniqueCharacters2(s):
    s1 = sorted(s)
    for i in range(len(s1)-1):
        if(s1[i] == s1[i+1]):
            return False
    return True

s = "absc10gd"

if uniqueCharacters(s):
    print("Unique")
else:
    print("Not unique")

if uniqueCharacters2(s):
    print("Unique")
else:
    print("Not unique")