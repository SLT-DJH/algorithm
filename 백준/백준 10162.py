T = int(input())

a = 0
b = 0
c = 0

getlist = [300, 60, 10]

if T % 10 != 0 :
    print(-1)
else :
    while T != 0 :
        if T // getlist[0] >= 1 :
            get = T // getlist[0]
            a += get
            
            T -= getlist[0] * get
        elif T // getlist[1] >= 1 :
            get = T // getlist[1]
            b += get
            
            T -= getlist[1] * get
        elif T // getlist[2] >= 1 :
            get = T // getlist[2]
            c += get
            
            T -= getlist[2] * get
    print(a, b, c)
