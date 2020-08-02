def printAllBinary(digits):
    printAllBinaryHelper(digits, '')

def printAllBinaryHelper(digits, output):
    if digits == 0:
        print(output, end='\n')
    else:
        printAllBinaryHelper(digits-1, output+'0')
        printAllBinaryHelper(digits-1, output+'1')

if __name__ == "__main__":
    printAllBinary(4)