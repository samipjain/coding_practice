from collections import defaultdict

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def detectCycleUtil(self, v, visited, recStack):
        if visited[v] == False:
            visited[v] = True
            recStack[v] = True

            for i in self.graph[v]:
                if not visited[i] and self.detectCycleUtil(i, visited, recStack):
                    return True
                elif recStack[i]:
                    return True
        recStack[v] = False
        return False               

    def detectCycle(self):
        # Dict for visited nodes
        visited = {}
        recStack = {}

        for i in range(self.V):
            visited[i] = False
            recStack[i] = False
        
        for v in range(self.V):
            if not visited[v] and self.detectCycleUtil(v, visited, recStack):
                return True

        return False
    
if __name__ == "__main__":
    g = Graph(4)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print(g.detectCycle())
