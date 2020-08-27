'''
Flexport

Given a keypad (like old phone), generate words from a given sequence-
PAD = {
    "1": ['a', 'b'],
    "2": ["c", "d"]
}

sequence can be -
1 = [a, b]
12 = [ac, ad, bc, bd]
112 = [aac, aad, abc, abd, bbc, bbd, bac, bad ]
121 = [aca, ada, acb, adb, bcb, bdb, bca, bda ]
1111222211
'''
PAD = {
    "1": ['a', 'b'],
    "2": ['c', 'd']
}

def getWords(seq):
    result = []
    return getWordsUtil(seq, result)
    # return result

def getWordsUtil(seq, result):
    if seq == '':
        return result

    result = findWords(PAD[seq[0]], result)

    return getWordsUtil(seq[1:], result)

def findWords(arr1, arr2):
    if len(arr2) == 0:
        return arr1
    
    return [i+j for i in arr2 for j in arr1]
    # else:
    #     result = []
    #     for i in arr2:
    #         for j in arr1:
    #             result.append(i+j)
    # return result

if __name__ == "__main__":
    print(getWords(''))
    print(getWords('1'))
    print(getWords('12'))
    print(getWords('121'))
    print(getWords('112'))
    print(getWords('112211'))