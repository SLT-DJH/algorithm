N = int(input())

line = input()
line = list(map(int, line.split()))

line.sort()

answer = []

get = 0

for i in range(N) :
    get += line[i]
    
    answer.append(get)

print(sum(answer))
