def validAnagram(s,t):
    if (len(s) != len(t)):
        return False
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(validAnagram(s,t))