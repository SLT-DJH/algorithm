def fibo(num) :
    if num == 1 :
        return 1
    elif num == 2 :
        return 1
    elif num == 3 :
        return 1
    else :
        num = num - 3

        a = 1
        b = 1
        c = 1

        while num != 0 :
            d = a + b
            a = b
            b = c
            c = d

            num = num - 1

        return c

a = int(input())

for _ in range(a) :
    get = int(input())

    print(fibo(get))

        
