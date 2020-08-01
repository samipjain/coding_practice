'''
We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears 
across all the bunnies recursively (without loops or multiplication).


bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
'''

def bunnyEars(n):
    if n == 0:
        return n
    return 2 + bunnyEars(n-1)

'''
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. 
The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return 
the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).


bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
'''
def bunnyEars2(n):
    if n == 0:
        return 0
    if n%2 == 1:
        return 2 + bunnyEars2(n-1)
    else:
        return 3 + bunnyEars2(n-1)

print(bunnyEars(4))
print(bunnyEars2(4))