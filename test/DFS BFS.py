def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
        if len(visit) == 6 :
            print(visit)

    return visit


if __name__ == "__main__":
    graph = {
        '1': ['2', '3'],
        '2': ['1', '3', '4'],
        '3': ['1', '2', '4', '5'],
        '4': ['2', '3', '5', '6'],
        '5': ['3', '4', '6'],
        '6': ['4', '6'],
    }

    print(bfs(graph, '1'))
    print(dfs(graph, '1'))
