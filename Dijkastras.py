import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances
graph = {}
n = int(input("Enter the number of nodes in the graph: "))

for i in range(n):
    node = input("Enter the name of node " + str(i + 1) + ": ")
    graph[node] = {}
    
    m = int(input("Enter the number of neighbors for node " + str(i + 1) + ": "))
    for j in range(m):
        neighbor, weight = input("Enter the name of neighbor " + str(j + 1) + " and its weight separated by space: ").split()
        graph[node][neighbor] = int(weight)

start = input("Enter the starting node: ")

distances = dijkstra(graph, start)

print("Shortest distances from node", start)
for node in distances:
    print(node, distances[node])

"""
Enter the number of nodes in the graph: 5
Enter the name of node 1: A
Enter the number of neighbors for node 1: 3
Enter the name of neighbor 1 and its weight separated by space: B 3
Enter the name of neighbor 2 and its weight separated by space: C 2
Enter the name of neighbor 3 and its weight separated by space: D 4
Enter the name of node 2: B
Enter the number of neighbors for node 2: 1
Enter the name of neighbor 1 and its weight separated by space: E 6
Enter the name of node 3: C
Enter the number of neighbors for node 3: 1
Enter the name of neighbor 1 and its weight separated by space: E 1
Enter the name of node 4: D
Enter the number of neighbors for node 4: 1
Enter the name of neighbor 1 and its weight separated by space: E 2
Enter the name of node 5: E
Enter the number of neighbors for node 5: 0
Enter the starting node: A

"""