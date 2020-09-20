def uclid(numa, numb) :

    if numa <= numb :
        x = numa
        y = numb
    else :
        x = numb
        y = numa

    temp = 0
    
    while y % x != 0 :
        temp = y % x
        y = x
        x = temp

    return x


t = int(input())

for i in range(t) :
    n = input()
    n = list(map(int, n.split()))

    case = n[0]

    del n[:1]

    total = 0

    for j in range(case-1) :
        for k in range(j+1, case) :
            total += uclid(n[j], n[k])
    print(total)



