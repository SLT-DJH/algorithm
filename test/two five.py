a = int(input())

get = a

twocount = 0
fivecount = 0

while get != 1 :
    tempget = get
    
    while True :
        if tempget % 2 == 0 :
            twocount += 1
            tempget = tempget // 2
        else :
            if tempget % 5 == 0 :
                fivecount += 1
                tempget = tempget // 5
            else :
                break

    get = get - 1

print(twocount, fivecount)
        
