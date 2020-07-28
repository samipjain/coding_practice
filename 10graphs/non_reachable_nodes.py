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

    def countNonReachableNodesUtil(self, v, visited):
        visited[v] = True

        for n in self.graph[v]:
            if not visited[n]:
                self.countNonReachableNodesUtil(n, visited)
    
    def countNonReachableNodes(self, start):
        visited = {}
        for vertex in self.getVertices():
            visited[vertex] = False

        self.countNonReachableNodesUtil(start, visited)

        result = []
        for vertex in self.getVertices():
            if not visited[vertex]:
                result.append(vertex)
        return result
    
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(6, 7)

    # g.printGraph()

    V = g.getVertices()
    E = g.getEdges()

    # print(V)
    # print(E)

    print(g.countNonReachableNodes(0))

    g2 = Graph()
    g2.addEdge("Samip", "Prafull")
    g2.addEdge("Samip", "Tony")
    g2.addEdge("Prafull", "Tony")
    g2.addEdge("Abhishek", "Phillip")
    g2.addEdge("Phillip", "Sarah")
    g2.addEdge("Abhishek", "Ashley")

    V2 = g2.getVertices()
    E2 = g2.getEdges()
    # g2.printGraph()

    # print(V2)
    # print(E2)
    print(g2.countNonReachableNodes("Abhishek"))
