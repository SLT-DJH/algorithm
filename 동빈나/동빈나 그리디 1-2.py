N, M, K = map(int, input().split())

getlist = list(map(int, input().split()))

getlist.sort()

first = getlist[N-1]
second = getlist[N-2]

get = M // (K+1)
left = M % (K+1)

answer = (get * ((K *first) + second)) + (left * first)

print(answer)
