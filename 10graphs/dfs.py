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

    def DFSUtil(self, s, visited):
        visited[s] = True
        print(s)

        for i in self.graph[s]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, s):
        visited = defaultdict()
        for i in self.graph.keys():
            visited[i] = False
        
        for v in self.graph.keys():
            if not visited[v]:
                self.DFSUtil(v, visited)

    
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

    g.DFS(0)

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

    # print(V2)
    # print(E2)

    # g2.DFS("Abhishek")
