def fibo(num) :
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    else :
        num = num - 2

        a = 1
        b = 2

        while num != 0 :
            c = (a+b) % 15746
            a = b
            b = c

            num = num - 1

        return b

a = int(input())
print(fibo(a))
