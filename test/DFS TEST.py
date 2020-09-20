def dfs_recursive(graph, start, visited=[]):
    
    visited = visited + [start] ## visited.append(start)대신 visited = visited + [start]를 대입
    if len(visited) == 6 :
        print(visited) # print(visited) 추가
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    
    return visited

graph = {
    '1': ['2', '3'],
    '2': ['1', '3', '4'],
    '3': ['1', '2', '4', '5'],
    '4': ['2', '3', '5', '6'],
    '5': ['3', '4', '6'],
    '6': ['4', '5']
    }


dfs_recursive(graph, '1')
