class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}
    
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print_graph(self):
        print(self.graph)
    
    def BFS(self, start):
        result = []
        queue = []
        queue.append(start)
        
        while queue:
            element = queue.pop(0)
            if element in result:
                break
            result.append(element)
            print(element)

            for i in self.graph[element]:
                queue.append(i)
        print(result)

    def BFS_2(self, start):
        queue = []
        visited = [False for i in range(self.V)]
        queue.append(start)
        visited[start] = True

        while queue:
            element = queue.pop(0)
            print(element)

            for i in self.graph[element]:
                if visited[i] is not True:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.print_graph()
    graph.BFS(2)
    graph.BFS_2(2)