def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        first = s[0]
        last = s[len(s)-1]
        middle = s[1:len(s)-2]

        if first == last and isPalindrome(middle):
            return True
        else:
            return False

if __name__ == "__main__":
    print(isPalindrome('raar'))