import math

def bossbattle(po) :
    global mlevel
    global mREM
    global mCUR
    global mATT
    global mDEF
    global mEXPCUR
    global mEXPMAX
    global mW
    global mA
    global mO
    
    if 'HU' in mO :
        mREM = mCUR
        
    startattack = 0
    firstget = 0

    monW = monsterW[po] ## 몬스터 공격력
    monA = monsterA[po] ## 몬스터 방어력
    monH = monsterH[po] ## 몬스터 최대체력

    if 'EX' in mO : ## 몬스터 경험치
        monE = math.trunc(monsterE[po] * 1.2)
    else :
        monE = monsterE[po]

    if 'HU' in mO :
        firstget = 1

    ## 아이템 확인
    if 'CO' in mO :
        if 'DX' in mO :
            startattack = (mATT + mW) * 3
        else :
            startattack = (mATT + mW) * 2

    while True :
        if startattack != 0 :
            monH -= max(1, (startattack - monA))
            startattack = 0
        else :
            monH -= max(1, ((mATT + mW) - monA))

        if monH <= 0 :
            break

        if firstget != 0 :
            firstget = 0
        else :
            mREM -= max(1, (monW - (mDEF + mA)))

        if mREM <= 0 :
            break

    if monH <= 0 : ## 이겼닭
        if 'HR' in mO :
            mREM += 3
            if mREM >= mCUR :
                mREM = mCUR

        mEXPCUR += monE
        if mEXPCUR >= mEXPMAX :
            mlevel += 1
            mEXPCUR = 0
            mEXPMAX = mlevel * 5

            mCUR += 5
            mREM = mCUR

            mATT += 2
            mDEF += 2

        return True

    if mREM <= 0 :
        return False  
def battle(po) :
    global mlevel
    global mREM
    global mCUR
    global mATT
    global mDEF
    global mEXPCUR
    global mEXPMAX
    global mW
    global mA
    global mO
    
    startattack = 0

    monW = monsterW[po] ## 몬스터 공격력
    monA = monsterA[po] ## 몬스터 방어력
    monH = monsterH[po] ## 몬스터 최대체력

    if 'EX' in mO : ## 몬스터 경험치
        monE = math.trunc(monsterE[po] * 1.2)
    else :
        monE = monsterE[po]

    ## 아이템 확인
    if 'CO' in mO :
        if 'DX' in mO :
            startattack = (mATT + mW) * 3
        else :
            startattack = (mATT + mW) * 2

    while True :
        if startattack != 0 :
            monH -= max(1, (startattack - monA))
            startattack = 0
        else :
            monH -= max(1, ((mATT + mW) - monA))

        if monH <= 0 :
            break

        mREM -= max(1, (monW - (mDEF + mA)))

        if mREM <= 0 :
            break

    if monH <= 0 : ## 이겼닭
        if 'HR' in mO :
            mREM += 3
            if mREM >= mCUR :
                mREM = mCUR

        mEXPCUR += monE
        if mEXPCUR >= mEXPMAX :
            mlevel += 1
            mEXPCUR = 0
            mEXPMAX = mlevel * 5

            mCUR += 5
            mREM = mCUR

            mATT += 2
            mDEF += 2

        return True

    if mREM <= 0 :
        return False      

def move(com, now, board) :
    x, y = now
    
    if com == 'L' :
        cx = x - 1
        cy = y
    elif com == 'R' :
        cx = x + 1
        cy = y
    elif com == 'U' :
        cx = x
        cy = y - 1
    elif com == 'D' :
        cx = x
        cy = y + 1

    if 1 <= cx < M+1 and 1 <= cy < N+1 and board[cy-1][cx-1] != '#' :
            return (cx, cy)
    else :
        return (x, y)

N, M = map(int, input().split())

board = []

monster = 0
item = 0

for i in range(N) :
    mlist = []

    get = str(input())

    for j in range(M) :
        if get[j] == '&' or get[j] == 'M':
            monster += 1
        elif get[j] == 'B' :
            item += 1
        elif get[j] == '@' :
            now = (j+1, i+1)
            mstart = (j+1, i+1)
        mlist.append(get[j])

    board.append(mlist)

command = str(input())

monsterposition = []
monstername = []
monsterW = []
monsterA = []
monsterH = []
monsterE = []

for i in range(monster) :
    R, C, S, W, A, H, E = input().split()
    monsterposition.append((int(C), int(R)))
    monstername.append(str(S))
    monsterW.append(int(W))
    monsterA.append(int(A))
    monsterH.append(int(H))
    monsterE.append(int(E))

itemposition = []
itemT = []
itemS = []

for i in range(item) :
    R, C, T, S = input().split()
    itemposition.append((int(C), int(R)))
    itemT.append(str(T))
    if str(T) == 'W' or str(T) == 'A' :
        itemS.append(int(S))
    else :
        itemS.append(str(S))

turn = 0
mlevel = 1
mREM = 20
mCUR = 20
mATT = 2
mDEF = 2
mEXPCUR = 0
mEXPMAX = mlevel * 5
mW = 0
mA = 0
mO = []

allcommand = 0

answer = ""

board[now[1]-1][now[0]-1] = '.'

for i in command :
    nextnow = move(i, now, board)
    turn += 1
    
    dx, dy = now
    x , y = nextnow

    if board[y-1][x-1] == '.' : ## nothing

        now = nextnow
    elif board[y-1][x-1] == '^' : ## trap
        if 'DX' in mO :
            mREM -= 1
        else :
            mREM -= 5
            
        if mREM <= 0 :
            if 'RE' in mO :
                mO.remove('RE')
                now = mstart
                mREM = mCUR

            else :
                allcommand = 1
                answer = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."

                break
        else :

            now = nextnow
    elif board[y-1][x-1] == 'B' : ## item
        po = itemposition.index((x, y))
        if itemT[po] == 'W' :
            mW = itemS[po]
        elif itemT[po] == 'A' :
            mA = itemS[po]
        elif itemT[po] == 'O' :
            if itemS[po] not in mO :
                if len(mO) < 4 :
                    mO.append(itemS[po])
        board[y-1][x-1] = '.'
        now = nextnow
    elif board[y-1][x-1] == '&' : ## monster
        po = monsterposition.index((x,y))
        if battle(po) :
            board[y-1][x-1] = '.'
            now = nextnow
        else :
            if 'RE' in mO :
                mO.remove('RE')
                now = mstart
                mREM = mCUR

            else :
                allcommand = 1
                answer = "YOU HAVE BEEN KILLED BY " + monstername[po] + ".."

                break
    elif board[y-1][x-1] == 'M' : ## boss
        po = monsterposition.index((x,y))
        if bossbattle(po) :
            board[y-1][x-1] = '@'
            allcommand = 1
            answer = "YOU WIN!"
            break
        else :
            if 'RE' in mO :
                mO.remove('RE')
                now = mstart
                mREM = mCUR

            else :
                allcommand = 1
                answer = "YOU HAVE BEEN KILLED BY " + monstername[po] + ".."

                break

if allcommand == 0 :
    board[now[1]-1][now[0]-1] = '@'
    answer = "Press any key to continue."

for i in board :
    tempget = ""
    for j in i :
        tempget += j
    print(tempget)

print("Passed Turns :", turn)
print("LV :", mlevel)
if mREM < 0 :
    mREM = 0
HP = str(mREM) + "/" + str(mCUR)
print("HP :", HP)
ATT = str(mATT) + "+" + str(mW)
print("ATT :", ATT)
DEF = str(mDEF) + "+" + str(mA)
print("DEF :", DEF)
EXP = str(mEXPCUR) + "/" + str(mEXPMAX)
print("EXP :", EXP)
print(answer)
