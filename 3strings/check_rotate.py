def findIndex(ch, b):
	result = []
	for i, c in enumerate(b):
		if c == ch:
			result.append(i)
	return result

def checkRotate(a, b):
    if a == '' and b == '':
        return True
    first_char = a[0]
    list_index = findIndex(first_char, b)
    flag = [True] * len(list_index)
	
    for idx, i in enumerate(list_index):
        index = i
        for ch in range(1, len(a)):
            if index == len(b)-1:
                index = -1
            if a[ch] == b[index+1]:
                index += 1
                continue
            else:
                flag[idx] = False
                break

    if True in flag:
        return True
    else:
        return False

if __name__ == "__main__":
    print(checkRotate('qweqe', 'qeqwe'))