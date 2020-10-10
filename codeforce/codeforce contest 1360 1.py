t = int(input())

for _ in range(t) :
    a, b = map(int, input().split())

    if a > b :
        x = a
        y = b
    else :
        x = b
        y = a


    if x > 2 * y :
        print(x ** 2)
    else :
        print((2*y) ** 2)
