def is_ok(num, current, start) :
    if current == [] :
        return True
    
    for i in range(len(current)) :
        if current[i] == num or abs(current[i]-num) == start - i:
            return False    
    return True

def DFS(N, start, current, final) :
    if start == N :
        final.append(current[:])
        return
    
    for i in range(N) :
        if is_ok(i, current, start) :
            current.append(i)
            DFS(N, start+1, current, final)
            current.pop()

N = int(input())

final = []

DFS(N, 0, [], final)

print(len(final))
