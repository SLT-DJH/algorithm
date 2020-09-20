def solve(a) :
    total = 0
    for i in range(len(a)) :
        total = total + a[i]
    print(total)

x = input()

x = list(map(int, x.split()))

solve(x)
