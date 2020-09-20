def BFS(number) :
    move = [number-1, number+1, number*2]

    for j in range(3) :
        if move[j] >= 0 and move[j] <= 100000 :
            if myposition[move[j]] != 1 :
                tempposition.append(move[j])
                myposition[move[j]] = 1

a = input()

a = list(map(int, a.split()))

N = a[0]

K = a[1]

count = 0

check = [0 for _ in range(100001)]
myposition = [0 for _ in range(100001)]

position = []

position.append(N)

tempposition = []

myposition[N] = 1


if N > K :
    count += (N - K)
else :
    while myposition[K] != 1 :
        count += 1
        for i in range(len(position)) :
            if check[position[i]] != 1 :
                BFS(position[i])
                check[position[i]] = 1
        position = tempposition
        tempposition = []

print(count)
