class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}
    
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print_graph(self):
        print(self.graph)
    
    def mostFollowers(self):
        maxF = 0
        coolest = -1
        for vertex in range(self.V):
            followers = 0
            for n in self.graph:
                if vertex in self.graph[n]:
                    followers += 1
            if followers > maxF:
                maxF = followers
                coolest = vertex
        return coolest

if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.print_graph()

    print(graph.mostFollowers())