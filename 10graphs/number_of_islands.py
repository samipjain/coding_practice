class Graph:
    def __init__(self, r, c, g):
        self.ROW = r
        self.COL = c
        self.graph = g

    def isSafe(self, i, j, visited):
        return (i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j])

    def dfs(self, i, j, visited):
        neighborRow = [-1, -1, -1, 0, 0, 1, 1, 1]
        neighborCol = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        visited[i][j] = True
        
        for k in range(8):
            if self.isSafe(i+neighborRow[k], j+neighborCol[k], visited):
                self.dfs(i+neighborRow[k], j+neighborCol[k], visited)


    def numIslands(self):
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0

        for r in range(self.ROW):
            for c in range(self.COL):
                if not visited[r][c] and self.graph[r][c] == 1:
                    self.dfs(r, c, visited)
                    count += 1
        return count

if __name__ == "__main__":
    # graph = [[1, 1, 0, 0, 0], 
    #     [0, 1, 0, 0, 1], 
    #     [1, 0, 0, 1, 1], 
    #     [0, 0, 0, 0, 0], 
    #     [1, 0, 1, 0, 1]]

    graph = [
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    
    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print(g.numIslands())