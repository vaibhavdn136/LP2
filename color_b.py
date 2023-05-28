class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def isSafe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] and color[i] == c:
                return False
        return True

    def graphColoringUtil(self, m, color, v, sol):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, color, c):
                color[v] = c
                if self.graphColoringUtil(m, color, v + 1, sol):
                    return True
                color[v] = 0

        return False

    def graphColoring(self, m):
        color = [0] * self.V
        sol = []
        if not self.graphColoringUtil(m, color, 0, sol):
            print("No solution exists.")
            return

        print("Solution:")
        for i in range(self.V):
            sol.append((i, color[i]))
            print("Vertex", i, "is colored with", color[i])

        return sol



N = int(input("Enter the number of vertices in the graph: "))

g = Graph(N)


print("Enter the adjacency matrix for the graph:")
for i in range(N):
    row = input().split()
    g.graph[i] = [int(val) for val in row]

num_colors = int(input("Enter the number of colors available: "))


g.graphColoring(num_colors)
