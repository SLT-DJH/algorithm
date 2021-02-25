def DFS(start, line, m, current, box) :

    if box == [] :

        if len(current) == m :
            box.append(current[:])
            return

        for i in range(m) :
            if line[start] != line[i] and i not in current :
                current.append(i)
                DFS(i, line, m, current, box)
                current.pop()
    else :
        return

    

t = int(input())

for _ in range(t) :
    n = int(input())

    line = list(map(int, input().split()))

    line = [0] + line

    box = []

    DFS(0, line, n+1, [0], box)

    if box == [] :
        print("NO")
    else :
        print("YES")

        get = box[0]

        for i in range(2, len(get)) :
            print(get[i-1], get[i])
