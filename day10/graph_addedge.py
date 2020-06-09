class AdjNode:
    def __init__(self, val):
        self.vertex = val
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    
    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of ", i)
            curr = self.graph[i]
            while curr:
                print(curr.vertex, "->")
                curr = curr.next
            print(" \n")

if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.print_graph()