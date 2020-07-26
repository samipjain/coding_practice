from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def printGraph(self):
        print(self.graph)

    def getVertices(self):
        return [i for i in self.graph.keys()]

    def getEdges(self):
        return [edge for edge in self.graph.values()]
    
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.printGraph()

    V = g.getVertices()
    E = g.getEdges()

    print(V)
    print(E)
