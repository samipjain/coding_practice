# convert to lower case
# remove punctuations
# split
# create a dict
# check for each word in an array, if this word exist then increment the count, else insert a key-value pair

def most_common_words(text):
    new_text = ""
    punctuations = [',', '.']
    for t in text.lower():
        if t not in punctuations:
            new_text += t
    
    words_list = new_text.split(' ')
    result = dict()

    for word in words_list:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    
    #sorted alphabetically and then sort by count
    words = sorted(result.items())
    return sorted(words, reverse=True, key=lambda x: x[1])

if __name__ == "__main__":
    text = "It was the best of times, it was the worst of times."
    print(most_common_words(text))