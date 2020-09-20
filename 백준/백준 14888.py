def calcul(current, numlist) :
    temp = 0

    for i in range(len(numlist)) :
        if i == 0 :
            temp = numlist[0]
        else :
            tempget = current[i-1]
            if tempget == "+" :
                temp = temp + numlist[i]
            elif tempget == "-" :
                temp = temp - numlist[i]
            elif tempget == "x" :
                temp = temp * numlist[i]
            elif tempget == "/" :
                if temp < 0 :
                    temp = (-temp) // numlist[i]
                    temp = -temp
                else :
                    temp = temp // numlist[i]

    return temp

def DFS(M, start, current, plus, minus, multi, divide, numlist, final) :
    if start == M :
        a = calcul(current[:], numlist)
        final.append(a)
        return

    for i in range(4) :
        if i == 0 :
            if plus != 0 :
                current.append('+')
                DFS(M, start + 1, current, plus-1, minus, multi, divide, numlist, final)
                current.pop()
        if i == 1 :
            if minus != 0 :
                current.append('-')
                DFS(M, start + 1, current, plus, minus-1, multi, divide, numlist, final)
                current.pop()
        if i == 2 :
            if multi != 0 :
                current.append('x')
                DFS(M, start + 1, current, plus, minus, multi - 1, divide, numlist, final)
                current.pop()
        if i == 3 :
            if divide != 0 :
                current.append('/')
                DFS(M, start + 1, current, plus, minus, multi, divide -1, numlist, final)
                current.pop()
    

N = int(input())

numlist = input()
numlist = list(map(int, numlist.split()))

getlist = input()
getlist = list(map(int, getlist.split()))

plus = getlist[0]
minus = getlist[1]
multi = getlist[2]
divide = getlist[3]

final = []

M = N-1

DFS(M, 0, [], plus, minus, multi, divide, numlist, final)

print(max(final))
print(min(final))
