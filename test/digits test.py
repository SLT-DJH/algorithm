num = 1117

get = str(num)

allsum = 10

while allsum >= 10 :
    allsum = 0
    
    for i in get :
        allsum += int(i)

    get = str(allsum)

print(allsum)
