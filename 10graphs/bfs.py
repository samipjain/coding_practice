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

    def BFS(self, s):
        q = []
        visited = defaultdict()
        for i in self.graph.keys():
            visited[i] = False
        result = []
        
        q.append(s)
        visited[s] = True
        
        while q:
            curr = q.pop(0)
            vertices = self.graph[curr]
            for v in vertices:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True
            
            result.append(curr)
        
        return result

    
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

    print(g.BFS(0))

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

    print(V2)
    print(E2)

    print(g2.BFS("Abhishek"))
