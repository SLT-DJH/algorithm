N, M, K = map(int, input().split())

getlist = list(map(int, input().split()))

getlist.sort()

getlist.reverse()

start = 0
maxnum = 0
count = 0
sumnum = 0
temp = 0


while M != 0 :
    if maxnum == 0 :
        maxnum = getlist[start]
        count += 1
        sumnum += maxnum
    else :
        if start == 0 :
            if count < K :
                sumnum += maxnum
                count += 1
            else :
                start = 1

                maxnum = getlist[start]

                count = 1
                sumnum += maxnum
        else :
            if count == 1 :
                start = 0
                maxnum = getlist[start]
                count = 1
                sumnum += maxnum
    M = M - 1

print(sumnum)
