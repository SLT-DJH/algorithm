from itertools import permutations

def cal(num, sick) :
    print(num)
    
    box = []
    take = []

    for i in num :
        a = i
        b = i+2
        left = sick[a-1]
        right = sick[b-1]
        calcul = sick[i]
        leftcount = -1
        rightcount = -1

        if box == [] :
            take.append(str(eval(left + calcul + right)))

            box.append([a,b])
        else :
            #check a
            for j in range(len(box)) :
                if a in box[j] :
                    left = take[j]

                    leftcount = j
            #check b
            for j in range(len(box)) :
                if b in box[j] :
                    right = take[j]

                    rightcount = j
                    
            temp = str(eval(left + calcul + right))

            if leftcount == -1 and rightcount == -1 :
                box.append([a,b])

                take.append(temp)
            elif leftcount == -1 :
                box[rightcount].append(a)

                take[rightcount] = temp
            elif rightcount == -1 :
                box[leftcount].append(b)

                take[leftcount] = temp
            else :
                box[rightcount].append(a)

                box[leftcount].append(b)

                take[leftcount] = temp

                take[rightcount] = temp
        print(box, take)

    return take


N = int(input())

sick = []

get = input()

for i in get :
    sick.append(i)

print(sick)

numlist = []

for i in range(N) :
    if (i+1) % 2 == 1 and (i+1) != N :
        numlist.append(i+1)

getall = list(permutations(numlist))

print(getall)

final = []

for i in getall :
    final.append(cal(list(i), sick))

print(final)
