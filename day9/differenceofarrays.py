# concat both arrays and keep unique values
# iterate over the new concatenated array and check if value exists in both input arrays
# if yes, then ignore; else append it the output array

def diff(arrA, arrB):
    if arrA is None and arrB is None: 
        return
    elif arrA is None and arrB is not None:
        return arrB
    elif arrA is not None and arrB is None:
        return arrA

    output = []
    for a in arrA:
        if a not in arrB:
            output.append(a)

    for b in arrB:
        if b not in arrA:
            output.append(b)
    return output

if __name__ == "__main__":
    # arrA = [1,2,3,4]
    # arrB = [3,4,5,6]
    arrA = [1,2,1]
    arrB = [2,1,2]
    print(diff(arrA, arrB))