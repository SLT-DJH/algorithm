n = int(input())

a = 1
b = 3
box = 0

if n == 1 :
    print(a)
elif n == 2 :
    print(b)
else :
    for i in range(3, n + 1) :
        box = b
        b = (2 * a) + b
        a = box
    print(b % 10007)
