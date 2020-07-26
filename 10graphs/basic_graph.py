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

    def printGraph(self):
        print(self.graph)

    def getVertices(self):
        return self.V

    def getEdges(self):
        return [self.graph[v] for v in self.V]
    
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

    g2 = Graph()
    g2.addEdge("Samip", "Prafull")
    g2.addEdge("Samip", "Abhishek")
    g2.addEdge("Prafull", "Abhishek")
    g2.addEdge("Prafull", "Samip")
    g2.addEdge("Abhishek", "Phillip")
    g2.addEdge("Abhishek", "Samip")
    g2.addEdge("Abhishek", "Sarah")
    g2.addEdge("Phillip", "Abhishek")
    g2.addEdge("Sarah", "Ashley")
    g2.addEdge("Sarah", "Abhishek")
    g2.addEdge("Ashley", "Sarah")

    V2 = g2.getVertices()
    E2 = g2.getEdges()
    g2.printGraph()

    print(V2)
    print(E2)
