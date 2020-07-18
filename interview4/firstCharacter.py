'''
Find the first repeating character from a given string
str = 'abcba', output = 'a' (not 'b')
'''

def firstCharacter(a):
    characters = []
    repeated = []

    for ch in a:
        if ch not in characters:
            characters.append(ch)
        else:
            repeated.append(ch)

    for ch in characters:
        if ch in repeated:
            return ch
    return False

if __name__ == "__main__":
    print(firstCharacter('abcba'))