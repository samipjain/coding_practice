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
        
            self.graph[src].append([dst, weight])
            self.graph[dst].append([src, 1/weight])

    def printGraph(self):
        print(self.graph)

    def getVertices(self):
        return self.V

    def getEdges(self):
        return [self.graph[v] for v in self.V]
    
    def getWeight(self, src, dst):
        # print("src", src, "dest", dst)
        queue = []
        queue.append(src)
        result = 1

        while queue:
            curr = queue.pop(0)
            if curr in self.graph:
                for adj in self.graph[curr]:
                    queue.append(adj[0])
                    print("resutl", adj[0], adj[1])
                    result = result * adj[1]
                    if adj[0] == dst:
                        break
                        
        return result


    def calcEquation(self, equations, values, queries):
        answer =  [0] * len(queries)
        
        self.addWeightedEdges(equations, values)

        for i, query in enumerate(queries):
            if query[0] == query[1]:
                answer[i] = -1.0 if query[0] not in self.V else 1.0
            elif query[0] not in self.V or query[1] not in self.V:
                answer[i] = -1.0
            else:
                answer[i] = self.getWeight(query[0], query[1])
        return answer

    
if __name__ == "__main__":
    g = Graph()

    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    # queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    queries = [ ["a", "c"] ]

    print(g.calcEquation(equations, values, queries))
    
