'''
Given (a,b) you can perform two operations
(a,b) = (a+b, b)
(a,b) = (a, a+b)

(a,b) should lead to (c,d) then return "Yes" else "No"

input = (1,1,5,2)
(1,1) => (1,2) => (3,2) => (5,2) 
'''

def isPossible(a, b, c, d):
    if a > c or b > d:
        return "No"
    
    if a == c and b == d:
        return "Yes"

    candidates = [(a,b)]

    while len(candidates) != 0:
        new_candidates = []
        for data in candidates:
            if data[0] == c and data[1] == d:
                return "Yes"
            
            if data[0] > c or data[1] > d:
                return "No"
            
            new_candidates.append((data[0]+data[1], data[1]))
            new_candidates.append((data[0], data[0]+data[1]))
        candidates = new_candidates
    
    return "No"

if __name__ == "__main__":
    print(isPossible(1,1,1000,1000))