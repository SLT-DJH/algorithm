def get(num) :
    box = []

    start = 2
    
    while num != 1 :
        if num % start == 0 :
            box.append(start)
            num = num // start
        else :
            start += 1

    return box

def lcm(boxa, boxb) :
    seta = set(boxa)
    setb = set(boxb)

    c = seta | setb

    lcmc = 1

    for i in c :
        a = boxa.count(i)
        b = boxb.count(i)

        if a < b :
            lcmc = lcmc * (i ** b)
        else :
            lcmc = lcmc * (i ** a)

    return lcmc

def lcs(boxa, boxb) :
    seta = set(boxa)
    setb = set(boxb)

    c = seta & setb

    lcsc = 1

    for i in c :
        a = boxa.count(i)
        b = boxb.count(i)

        if a < b :
            lcsc = lcsc * (i ** a)
        else :
            lcsc = lcsc * (i ** b)

    return lcsc

a, b = map(int, input().split())

boxa = get(a)
boxb = get(b)

print(lcs(boxa, boxb))
print(lcm(boxa, boxb))

