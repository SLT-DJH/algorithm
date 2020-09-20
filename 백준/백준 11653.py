def get(num) :
    box = []

    start = 2
    
    while num != 1 :
        if num % start == 0 :
            box.append(start)
            num = num // start
        else :
            start += 1

    box.sort()

    return box

a = int(input())

boxa = get(a)

for num in boxa :
    print(num)
