from itertools import combinations

#알파벳과 순서 딕셔너리 만들기

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

alphabet = alphabet.split()

alnum = {}

numal = {}

for i in range(len(alphabet)) :
    alnum[alphabet[i]] = i+1

for i in range(len(alphabet)) :
    numal[i+1] = alphabet[i]

#입력 받기

a = input()

a = list(map(int, a.split()))

L = a[0]

C = a[1]

mo = ['a', 'e', 'i', 'o', 'u']


alpha = input()
alpha = alpha.split()

#모음을 찾아서 모음과 자음으로 나누기
findmo = []

for i in range(len(alpha)) :
    if alpha[i] in mo :
        findmo.append(alpha[i])

for i in range(len(findmo)) :
    alpha.remove(findmo[i])

findja = alpha

#조합 시작

combination = []

for i in range(1, (L-2)+1) :
    combimo = list(combinations(findmo, i))
    combija = list(combinations(findja, L-i))
    for j in range(len(combimo)) :
        for k in range(len(combija)) :
            go = combimo[j] + combija[k]
            combination.append(list(go))

#조합 정렬

for i in range(len(combination)) :
    for j in range(L) :
        combination[i][j] = alnum[combination[i][j]]

for i in range(len(combination)) :
    combination[i].sort()

combination.sort()

for i in range(len(combination)) :
    for j in range(L) :
        combination[i][j] = numal[combination[i][j]]
        
#조합 출력
for i in range(len(combination)) :
    answer = ''
    for j in range(L) :
        answer += combination[i][j]
    print(answer)

