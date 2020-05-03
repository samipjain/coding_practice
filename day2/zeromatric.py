# Time Complexity: O(NxM) Space complexity O(N+M)
def zeroMatrix(mat):
    N = len(mat)
    M = len(mat[0])

    row_set, col_set = set(), set()

    for i in range(N):
        for j in range(M):
            if(mat[i][j] == 0):
                row_set.add(i)
                col_set.add(j)
    
    for i in range(N):
        for j in range(M):
            if i in row_set or j in col_set:
                mat[i][j] = 0
    print(mat)

mat = [
    [1,2,3,4],
    [5,0,7,8],
    [9,10,11,12]
]

zeroMatrix(mat)