def isValid(grid, row, col):
    print(row, " ",col)
    return grid[row][col]

def isAtEnd(grid, row, col):
    return row == 0 and col == 0

def countPaths(grid, row, col):
    if row >= 0 and col >= 0:
        if isValid(grid, row, col):
            return 0
        if isAtEnd(grid, row, col):
            return 1
        return countPaths(grid, row-1, col) + countPaths(grid, row, col-1)

if __name__ == "__main__":
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]

    row, col = len(grid)-1, len(grid[0])-1

    print(countPaths(grid, row, col))