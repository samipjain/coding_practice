'''
Given two strings, first is the key password that a user will type and second string is for keypad. Moving to adjacent key 
taake 1 second.
Like moving from 1 to 2 takes 1 second and moving from 1 to 3 takes 2 seconds

Find the total time taken by key password

keypad = '123456789'
1 2 3
4 5 6
7 8 9
key password = '25679'
output = 0 + 1 + 1 + 2 + 2 = 6
'''

def addNeighbors(x, y, keypad_list):
    result = []

    result.append(keypad_list[x-1][y-1])
    result.append(keypad_list[x-1][y])
    result.append(keypad_list[x-1][y+1])
    result.append(keypad_list[x][y-1])
    result.append(keypad_list[x][y+1])
    result.append(keypad_list[x+1][y-1])
    result.append(keypad_list[x+1][y])
    result.append(keypad_list[x+1][y+1])
    
    return result

def keypadTime(s, keypad):
    neighbors = dict()

    keypad_list = [[-1 for i in range(5)]]
    keypad_temp_list = []
    counter = 1

    for ch in keypad:
        if counter%5 == 1:
            keypad_temp_list.append(-1)
            keypad_temp_list.append(ch)
            counter += 1
        elif counter%4 == 0:
            keypad_temp_list.append(ch)
            keypad_temp_list.append(-1)
            keypad_list.append(keypad_temp_list)
            keypad_temp_list = []
            counter = 0
        else:
            keypad_temp_list.append(ch)
        counter += 1
    
    keypad_list.append([-1 for i in range(5)])
    print(keypad_list)
    
    for x in range(1,4):
        for y in range(1,4):
            neighbors[keypad_list[x][y]] = addNeighbors(x, y, keypad_list)
    time = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        if s[i] not in neighbors[s[i-1]]:
            time += 2
        else:
            time += 1
    return time

if __name__ == "__main__":
    print(keypadTime('1234', '923857614'))