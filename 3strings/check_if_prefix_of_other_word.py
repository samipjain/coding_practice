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

def isPrefixOfWord2(sentence, searchWord):
    word_list = sentence.split(' ')
    len_searchWord = len(searchWord)
    # check each word if it has prefix
    for i in range(len(word_list)):
        if word_list[i][:len_searchWord] == searchWord:
            return i+1
    return -1

if __name__ == "__main__":
    print(isPrefixOfWord("i love eating burger", "burg"))
    print(isPrefixOfWord("hellohello hellohellohello", "ell"))
    print(isPrefixOfWord2("i love eating burger", "burg"))
    print(isPrefixOfWord2("hellohello hellohellohello", "ell"))