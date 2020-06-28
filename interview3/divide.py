def digit(number):
    count = 0
    for i in range(0, len(number)):
        for j in range(i+1, len(number)+1):
            if int(number[i]) != 0:
                print(int(number[i:j]), number[i:j])
                if (int(number[i:j]) % 3 == 0):
                    count += 1
            elif len(number[i:j]) == 1 and number[i:j] == '0':
                count += 1
    return count
if __name__ == "__main__":
    print(digit('303'))