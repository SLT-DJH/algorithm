def linesum(line, m) :

    box = []
    
    temp = m//2
    
    po = []

    for i in range(temp) :
        po.append(i)

    until = []

    for i in range(temp) :
        until.append(m - temp + i)

    while po[0] != until[0] :
        tempsum = 0

        for i in range(temp) :
            tempsum += line[po[i]]

        box.append(tempsum)
        
        
        check = 0
        
        for i in range(temp) :
            if po[i] == until[i] :
                check = 1
                po[i-1] += 1

                for k in range(i, temp) :
                    po[k] = po[k-1] + 1

                break
            
        if check == 0 :
            po[temp-1] += 1

    tempsum = 0

    for i in range(temp) :
        tempsum += line[po[i]]

    box.append(tempsum)

    box.sort(reverse=True)

    return box

print(linesum([1,2,3,4,5,6], 6))
