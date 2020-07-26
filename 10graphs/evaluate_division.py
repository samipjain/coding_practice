from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = []
        self.graph = defaultdict(list)

    def addWeightedEdges(self, equations, values):
        for i in range(len(equations)):
            src, dst = equations[i]
            weight = values[i]
            
            if src not in self.V:
                self.V.append(src)
            if dst not in self.V:
                self.V.append(dst)
        
            self.graph[src].append({dst, weight})

    def printGraph(self):
        print(self.graph)

    def getVertices(self):
        return self.V

    def getEdges(self):
        return [self.graph[v] for v in self.V]

    def calcEquation(self, equations, values, queries):
        self.addWeightedEdges(equations, values)

    
if __name__ == "__main__":
    g = Graph()

    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

    g.calcEquation(equations, values, queries)

    g.printGraph()
    
