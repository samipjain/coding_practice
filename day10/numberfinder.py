def find_first(arr, num):
    index = 0
    for i in arr:
        if i == num:
            return index
        index += 1
    return -1

if __name__ == "__main__":
    arr = [200, 200, 200, 500, 200]
    print(find_first(arr, 200))