from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def canFinish(self, numCourses, prerequisites):
        # Dict for visited nodes
        visited = {}

        for dst, src in prerequisites:
            visited[src] = visited[dst] = False
            self.graph[src].append(dst)

        recStack = visited.copy()

        for node in range(numCourses):
            if not visited[node] and self.isCycle(node, visited, recStack):
                return False
        return True

    def isCycle(self, node, visited, recStack):
        if not visited[node]:
            visited[node] = True
            recStack[node] = True

        for n in self.graph[node]:
            if not visited[n] and self.isCycle(n, visited, recStack):
                return True
            elif recStack[n]:
                return True

        recStack[node] = False
        return False


    
if __name__ == "__main__":
    g = Graph()

    numCourses = 4
    prereq = [[1,0], [2,1], [3,2]]
    # prereq = [[1,0], [0,1]]
    # prereq = [[1,0]]
    print(g.canFinish(numCourses, prereq))
