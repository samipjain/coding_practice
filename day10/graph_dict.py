class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}
    
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def print_graph(self):
        for i in range(self.V):
            print(i, "->", self.graph[i])

if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.print_graph()