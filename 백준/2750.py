N = int(input())

answer = []

for i in range(N) :
    a = int(input())

    answer = answer + [a]

answer.sort()

for i in range(N) :
    print(answer[i])
