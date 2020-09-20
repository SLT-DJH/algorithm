parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1
                
def kruskal(graph):    
    for v in graph['vertices']:
        make_set(v)
        
    mst = []
    
    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    
    return mst

graph = {}

graph['vertices'] = []
graph['edges'] = []

N = int(input())

for i in range(N) :
    graph['vertices'].append(str(i+1))

M = int(input())

for i in range(M) :
    line = input()

    line = list(map(int, line.split()))

    get = (line[2], str(line[0]), str(line[1]))

    graph['edges'].append(get)

answer = kruskal(graph)

total = 0

for i in range(len(answer)) :
    total += answer[i][0]

print(total)
