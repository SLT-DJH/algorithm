T = int(input())

for i in range(T) :
    p = input()
    n = int(input())
    a = input()
    getlist = []
    strset = ""
    way = 0
    contin = 0

    for i in a :
        if i == "[" :
            continue
        elif i == "," or i == "]":
            if strset != "" :
                getlist.append(int(strset))
            strset = ""
        else :
            strset = strset + i

    if p.count('D') > len(getlist) :
        print('error')
    elif p.count('D') == len(getlist) :
        print('[]')
    else :
        for i in p :
            if i == 'R' :
                if contin == 0 :
                    contin = 1
                else :
                    contin += 1
            else :
                if contin % 2 == 0 :
                    way = 0
                else :
                    way = 1

                if way == 0 :
                    getlist = getlist[1:]
                else :
                    getlist.reverse()
                    getlist = getlist[1:]

                contin = 0
                way = 0

        print(getlist)
                
            

                
        

    
