import collections

def dfs(V):
  S = []
  visited = []
  result = ""
  while True:
    if V in visited: 
      break
    result += f'{V} '
    visited.append(V)
    
    for i in reversed(sorted(list(A[V]))):
      if i not in visited:
        S.append(i)

    if (len(S) <= 0): 
      break
      
    V = S.pop()
    
  print(result.rstrip())

def bfs(V):
  Q = collections.deque()
  visited = [V]
  result = ""
  while True:
    result += f'{V} '

    for i in sorted(list(A[V])):
      # 한번도 방문하지 않았을 때
      if i not in visited:
        visited.append(i)
        Q.append(i)

    if not Q: 
      break
    V = Q.popleft()

  print(result.rstrip(), end="")

# N = 정점, M = 간선, V = start node name
N, M, V = map(int, input().split(" "))
# 인접리스트
A = { V: set() }
for i in range(M):
  b, c = map(int, input().split(" "))
  # 처음 들어온 node는 빈 set을 만들어준다.
  if b not in A:
    A[b] = set()
  if c not in A:
    A[c] = set()

  # 서로의 인접리스트에 서로를 추가해준다.
  A[b].add(c)
  A[c].add(b)

dfs(V)
bfs(V)
