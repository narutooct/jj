def get_weight(edge):
    return edge[2]
def kruskal(graph):
    edges = sorted(graph, key=get_weight)
    parent = list(range(len(edges) + 1))
    for edge in edges:
        u, v, w = edge
        pu, pv = parent[u], parent[v]
        if pu != pv:
            print(u,"-",v,":",w)
            for i in range(len(parent)):
                if parent[i] == pv:
                    parent[i] = pu

n = int(input("Enter the no of nodes: "))        
G=[]
for i in range(n):
    G.append(list(map(int, input().split())))
print("Edge : Weight")
("graph=[[0 ,1 ,2], [0 ,3 ,6], [1 ,2 ,3], [1 ,4 ,5], [2 ,4 ,7], [3 ,4 ,9]]")
kruskal(G)
