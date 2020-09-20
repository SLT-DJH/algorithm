alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = []

for i in range(len(alphabet)) :
    alpha.append(alphabet[i])

N = int(input())

sick = input()

sickbox = []

for i in range(len(sick)) :
    sickbox.append(sick[i])

numbox = []

calcul = []

for i in range(N) :
    put = int(input())

    numbox.append(put)

alphanum = {}

for i in range(N) :
    alphanum[alpha[i]] = numbox[i]
    
for i in range(len(sickbox)) :
    if sickbox[i] == '+' :
        x = calcul.pop()
        y = calcul.pop()
        total = y + x
        calcul.append(total)
    elif sickbox[i] == '-' :
        x = calcul.pop()
        y = calcul.pop()
        total = y - x
        calcul.append(total)
    elif sickbox[i] == '*' :
        x = calcul.pop()
        y = calcul.pop()
        total = y * x
        calcul.append(total)
    elif sickbox[i] == '/' :
        x = calcul.pop()
        y = calcul.pop()
        total = y / x
        calcul.append(total)
    else :
        calcul.append(alphanum[sickbox[i]])

print('%.2f' % calcul[0])
    
