def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] == 2 * arr[i] or arr[i] == 2 * arr[j] and i != j:
                return True
    return False

if __name__ == "__main__":
    print(checkIfExist([1,2]))