def prime(num) :
    if num <= 1 :
        return False
    i = 2
    while i * i <= num :
        if num % i == 0 :
            return False
        i += 1
    return True

def myCM(x) :

    temp = x
    box = [1]

    if temp == 1 :
        return box
    elif temp in skip :
        box.append(x)
        return box
    else :
        count = 1

        while temp != 1 and count != temp:
            count += 1

            if temp % count == 0 :
                box.append(count)
                temp = temp / count
                count = count - 1
    
    return box

def LCM(a, b) :
    x = a
    y = b

    listx = myCM(x)
    listy = myCM(y)

    checkx = set(listx)
    checky = set(listy)

    check = checkx | checky

    check = list(check)

    total = 1

    for i in check :
        if listx.count(i) == 0 and listy.count(i) == 0 :
            continue
        else :
            if listx.count(i) >= listy.count(i) :
                total = total * (i ** listx.count(i))
            else :
                total = total * (i ** listy.count(i))

    return(total)

T = int(input())

for i in range(T) :
    case = input()
    case = list(map(int, case.split()))

    if case[0] < case[1] :
        A = case[0]
        B = case[1]
    else :
        A = case[1]
        B = case[0]

    skip = []

    for i in range(1, B+1) :
        if prime(i) :
            skip.append(i)

    print(LCM(A, B))
