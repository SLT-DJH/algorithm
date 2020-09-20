N = int(input())

take = []

for _ in range(N) :
    a = input()
    
    a = list(map(int, a.split()))
    
    take.append([a[1], a[0]])

take.sort()

for i in take :
    print(str(i[1]), str(i[0]))
