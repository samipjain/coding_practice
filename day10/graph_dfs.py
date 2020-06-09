class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}
    
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print_graph(self):
        print(self.graph)

    def DFSUtils(self, start, visited):
        visited[start] = True
        print(start)

        for i in self.graph[start]:
            if visited[i] is not True:
                self.DFSUtils(i , visited)
    
    def DFS(self, start):
        visited = [False for i in range(self.V)]

        self.DFSUtils(start, visited)

if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    graph.print_graph()
    graph.DFS(2)