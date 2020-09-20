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

graph = {
'vertices' : ['1', '2', '3', '4', '5', '6'],
'edges' : [
    (2, '2', '3'),
    (3, '4', '5'),
    (4, '1', '3'),
    (5, '1', '2'),
    (6, '3', '4'),
    (7, '2', '4'),
    (8, '4', '6'),
    (8, '4', '5')
    ]
}

print( kruskal(graph) )
