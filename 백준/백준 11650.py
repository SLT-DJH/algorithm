N = int(input())

take = []

for _ in range(N) :
    a = input()
    
    a = list(map(int, a.split()))
    
    take.append(a)

take.sort()

for i in take :
    print(str(i[0]), str(i[1]))
