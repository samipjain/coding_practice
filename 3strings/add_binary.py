def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # Obvious solution
    add = str(bin(int(a, 2) + int(b, 2)))
    return add[2:]

def addBinary2(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # Obvious solution
    add = str(bin(int(a, 2) + int(b, 2)))
    return add[2:]

if __name__ == "__main__":
    print(addBinary2('11', '1'))