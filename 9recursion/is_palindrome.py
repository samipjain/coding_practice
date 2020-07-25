def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        first = s[0]
        last = s[len(s)-1]
        middle = s[1:len(s)-2]

        return first == last and isPalindrome(middle)

if __name__ == "__main__":
    print(isPalindrome('raar'))