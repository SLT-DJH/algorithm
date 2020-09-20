def getscore(board, first, second) :
    firstscore = 0
    secondscore = 0

    for i in first :
        for j in first :
            firstscore += board[i-1][j-1]

    for i in second :
        for j in second :
            secondscore += board[i-1][j-1]

    return abs(firstscore - secondscore)

from itertools import combinations

N = int(input())

board = []

for _ in range(N) :
    line = input()

    line = list(map(int, line.split()))

    board.append(line)

num = [i+1 for i in range(N)]

combi = list(combinations(num, N//2))

first = combi[:len(combi)//2]
second = combi[len(combi)//2:]
second.reverse()

final = []

for i in range(len(first)) :
    final.append(getscore(board, first[i], second[i]))

print(min(final))
