get = input()

tempget = ""

laser = 0

for i in range(len(get)) :
    if i < len(get) - 1 :
        if laser == 0 :
            if get[i] == "(" and get[i+1] == ")" :
                tempget += "|"
                laser = 1
            else :
                tempget += get[i]
        else :
            laser = 0
            continue
    else :
        if laser == 0 :
            tempget += get[i]
        else :
            laser = 0
            continue

print(tempget)

stick = 0

tempstick = 0

stickcount = 0

for i in range(len(tempget)) :
    if tempget[i] == "|" :
        stick += tempstick + stickcount
        tempstick = 0
    elif tempget[i] == "(" :
        stickcount += 1
    elif tempget[i] == ")" :
        stickcount -= 1
        tempstick += 1
stick += tempstick

print(stick)
