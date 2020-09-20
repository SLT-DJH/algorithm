graph = { 0 : [1, 2], 1: [3,4], 2 : [5, 6] }

def dfs_recursive(graph, start, visited=[]) :

    for node in graph[start] :
        visited = visited + [node]
        if len(visited) == 3 :
            print(visited)
        if start + 1 < 3 :
            dfs_recursive(graph, start+1, visited)
        visited.pop()

    return visited

dfs_recursive(graph, 0)
