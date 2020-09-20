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

    print(round((n[0] * n[1]) / uclid(n[0], n[1])))



