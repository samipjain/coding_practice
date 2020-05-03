# You can perform insert, replace or remove a character from a string
# Given two strings, check if they are one edit(or zero edit) away
# "pale", "ple" = True
# "pale", "bale" = True
# "pale", "pales" = True
# "pale", "bake" = False

str1 = "pale"
str2 = "ple"

count = 0

# Replace
if (len(str1) == len(str2)):
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            count += 1
else:
    diff = len(str1) - len(str2)
    if (abs(diff) > 1):
        count = diff

if (count > 1):
    print("False")
else: 
    print("True")

