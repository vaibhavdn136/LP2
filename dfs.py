graph = {
    'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]
}

dfsvisited = set()

def dfs(dfsvisited, graph, root):
    if root not in dfsvisited:
        print(root, end=" ")
        dfsvisited.add(root)
        for neighbour in graph[root]:
            dfs(dfsvisited,graph,neighbour)
            
            
            

bfsvisited = []
queue = []

def bfs(bfsvisited, graph, node):
    bfsvisited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        
        for neighbour in graph[m]:
            if neighbour not in bfsvisited:
                bfsvisited.append(neighbour)
                queue.append(neighbour)
                


            
            
print("Following is the depth-first search")            
dfs(dfsvisited, graph, 'A')

print()

print("following is the breadth-first search")
bfs(bfsvisited, graph, 'A')