'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
'''

def backspaceCompare(S, T):
    s_arr = []
    t_arr = []

    for char in S:
        if char == '#':
            if s_arr:
                s_arr.pop()
        else:
            s_arr.append(char)

    for char in T:
        if char == '#':
            if t_arr:
                t_arr.pop()
        else:
            t_arr.append(char)

    return s_arr == t_arr

if __name__ == "__main__":
    print(backspaceCompare("ab#c", "ad#c"))
    print(backspaceCompare("ab##", "c#d#"))
    print(backspaceCompare("a##c", "#a#c"))
    print(backspaceCompare("a#c", "b"))