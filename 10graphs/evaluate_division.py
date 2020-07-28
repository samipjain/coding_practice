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
    
    def getWeightUtil(self, v, d, visited, result):
        print("src: ", v, "dst: ", d)
        print("result", result)
        visited[v] = True

        if v == d:
            return result
        else:
            for n in self.graph[v]:
                if not visited[n[0]]:
                    result = result * n[1]
                    return self.getWeightUtil(n[0], d, visited, result)

    def getWeight(self, src, dst):
        visited = defaultdict()
        result = 1
        for vertex in self.V:
            visited[vertex] = False

        
        if not visited[src]:
            result = self.getWeightUtil(src, dst, visited, result)
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

    # equations = [ ["a", "b"], ["b", "c"] ]
    # values = [2.0, 3.0]
    # queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    # queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    queries = [["x2", "x4"]]
    

    print(g.calcEquation(equations, values, queries))
    
