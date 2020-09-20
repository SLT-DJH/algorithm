while True :
    x = int(input())
    y = int(input())

    a = (3 * (x//3)) + (y//3)
    b = 3 * (x%3) + (y%3)

    print(a,b)
