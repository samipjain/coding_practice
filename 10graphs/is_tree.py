from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = []
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        if v not in self.V:
            self.V.append(v)
        if w not in self.V:
            self.V.append(w)
        self.graph[v].append(w)
        self.graph[w].append(v)

    def printGraph(self):
        print(self.graph)

    def getVertices(self):
        return self.V

    def getEdges(self):
        return [self.graph[v] for v in self.V]
    
    def isCycleUtil(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.isCycleUtil(i, visited, v):
                    return True
            elif i != parent:
                return True
        return False

    def isTree(self):
        visited = {}
        for v in self.V:
            visited[v] = False

        # Check if cycle exists, return False
        if self.isCycleUtil(self.V[0], visited, -1):
            return False

        # Check if all the vertices are visited, else return False
        for v in self.V:
            if not visited[v]:
                return False
        
        return True
    
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(3, 4)

    g.printGraph()

    print(g.isTree())

    g1 = Graph()
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(0, 3)
    g1.addEdge(1, 2)
    g1.addEdge(3, 4)

    print(g1.isTree())


    # g2 = Graph()
    # g2.addEdge("Samip", "Prafull")
    # g2.addEdge("Samip", "Abhishek")
    # g2.addEdge("Prafull", "Abhishek")
    # g2.addEdge("Prafull", "Samip")
    # g2.addEdge("Abhishek", "Phillip")
    # g2.addEdge("Abhishek", "Samip")
    # g2.addEdge("Abhishek", "Sarah")
    # g2.addEdge("Phillip", "Abhishek")
    # g2.addEdge("Sarah", "Ashley")
    # g2.addEdge("Sarah", "Abhishek")
    # g2.addEdge("Ashley", "Sarah")

    # V2 = g2.getVertices()
    # E2 = g2.getEdges()
    # g2.printGraph()

    # print(V2)
    # print(E2)
