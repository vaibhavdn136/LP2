def find(graph, node):
    if graph[node] < 0:
        return node
    else:
        temp = find(graph, graph[node])
        graph[node] = temp
        return temp
    

def union(graph, a, b, weight, answer):
    ta = chr(ord('A') + a - 1)  # Convert the node values to characters
    tb = chr(ord('A') + b - 1)
    a = find(graph, a)
    b = find(graph, b)
    if a == b:
        pass
    else:
        answer.append([ta, tb, weight])  # Include the weight in the answer
        if graph[a] < graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b


ipt = [[1, 2, 1], [1, 3, 3], [2, 6, 4], [3, 6, 2], [3, 4, 1], [4, 5, 5], [6, 7, 2], [6, 5, 6], [7, 5, 7]]
n = 7

answer = []
ipt = sorted(ipt, key=lambda ipt: ipt[2])
graph = [-1] * (n + 1)
total_weight = 0  # Variable to keep track of the total weight

for u, v, d in ipt:
    if find(graph, u) != find(graph, v):  # Check if adding the edge creates a cycle
        union(graph, u, v, d, answer)  # Pass the weight to the union function
        total_weight += d  # Update the total weight

for item in answer:
    print(item)

print("Total weight of minimum spanning tree:", total_weight)
