def digit(n):
    product = 1
    sum = 0
    for char in str(n):
        print(char)
        product = product * int(char)
        sum = sum + int(char)
    print(product)
    print(sum)
    return product - sum

if __name__ == "__main__":
    print(digit(123456))