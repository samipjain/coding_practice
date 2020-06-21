def isPrefixOfWord(sentence, searchWord):
    """
    :type sentence: str
    :type searchWord: str
    :rtype: int
    """
    # list of words
    word_list = sentence.split(' ')
    index = -1
    # check each word if it has prefix
    for i in range(len(word_list)):
        if word_list[i][0] == searchWord[0] and searchWord in word_list[i]:
            return i+1
    return -1

if __name__ == "__main__":
    print(isPrefixOfWord("i love eating burger", "burg"))
    print(isPrefixOfWord("hellohello hellohellohello", "ell"))