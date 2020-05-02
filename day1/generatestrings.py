# Count of strings can be formed using a,b,c with atmost 1 b and 2 c's

def generateStrings(n, b_count, c_count):
    if (b_count < 0 or c_count < 0):
        return 0
    if n == 0:
        return 1
    if b_count == 0 and c_count == 0:
        return 1

    res = generateStrings(n-1, b_count, c_count)
    res += generateStrings(n-1, b_count - 1, c_count)
    res += generateStrings(n-1, b_count, c_count - 1)

    return res

if __name__ == "__main__":
    n = 4
    b_count = 1
    c_count = 2
    print(generateStrings(n, b_count, c_count))
    