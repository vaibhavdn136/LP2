class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph=[[0 for _ in range (vertices)]for _ in range(vertices)]
        self.min_colours = float("inf")
    def isSafe(self , v , colour , c):
        for i in range (self.V):
            if self.graph[v][i] and colour[i]==c:
                return False
        return True
    def solvecolouringGraphutil(self, m,colour,v,sol):
        if v==self.V:
            
            if len(set(colour))<self.min_colours :
                self.min_colours =len(set(colour))
                sol.clear()
                
                for i in range (self.V):
                    sol.append((i,colour[i]))
            return True
        for c in range(1,m+1):
            if self.isSafe(v , colour , c):
                colour[v]=c
                if self.solvecolouringGraphutil(m,colour,v+1,sol):
                    return True
                colour[v]=0
        return False
    
    def graphcolouring(self,m):
        colour = [0]*self.V
        sol=[]
        if not self.solvecolouringGraphutil(m,colour,0,sol):
            print("solution does not exist")
            return 
        
        print("minimum numbers of colours:",self.min_colours)
        print("solution")
        for i in range(self.V):
            print("the vertex",sol[i][0],"has the colour:",sol[i][1])
        return sol
    
N = int(input("enter the number of vertices:"))

g = Graph(N)

print("Enter the adjecency matrix :")

for i in range(N):
    row = input().split()
    g.graph[i]=[int(val) for val in row]
    
num_colouring=int(input("enter the number of colouring:"))

g.graphcolouring(num_colouring)