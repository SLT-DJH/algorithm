prep = ["steed", "king", "first-born"]
pastp = ["mother", "father", "grandmother", "grandfather", "godfather"]
noun = ["hamster", "coconut", "duck", "herring", "newt", "peril", "chicken", "vole", "parrot", "mouse", "twit"]
prev = ["is", "masquerades as"]
pastv = ["was", "personified"]
adjective = ["silly","wicked","sordid","naughty","repulsive","malodorous","ill-tempered"]
adverb = ["conspicuously","categorically", "positively", "cruelly", "incontrovertibly"]

prepnum = 1
pastpnum = 1
nounnum = 1
prevnum = 1
pastvnum = 1
adjectnum = 1
adverbnum = 1
modinum = 1
modinounnum = 1
sentennum = 1
tauntnum = 1

def taunt() :

    global tauntnum
    global sentennum
    global pastpnum
    global pastvnum
    global modinounnum
    global prepnum
    global prevnum
    global nounnum
    
    a = tauntnum % 4

    tauntnum += 1

    if a == 1 :
        answer = senten()
    elif a == 2 :
        tempan = taunt()

        answer = tempan[:len(tempan)-1] + " " + senten()
        
    elif a == 3 :
        answer = nouni() + "!"
    elif a == 0 :
        answer = senten()

    temp = answer[0].upper()

    return temp + answer[1:] + "."

def senten() :

    global sentennum
    global pastpnum
    global pastvnum
    global modinounnum
    global prepnum
    global prevnum
    global nounnum
    
    a = sentennum % 3

    sentennum += 1

    if a == 1 :
        answer = pastrel() + " " + nounph()
        return answer
    elif a == 2 :
        answer = presentrel() + " " + nounph()
        return answer
    elif a == 0 :
        answer = pastrel() + " a " + nouni()
        return answer

def nounph() :

    global modinounnum
    global nounnum
    global modinum
    
    answer = "a " + modinoun()

    return answer

def modinoun() :

    global modinounnum
    global nounnum
    global modinum
    
    a = modinounnum % 2

    modinounnum += 1
    
    if a == 1 :
        return nouni()
    elif a == 0 :
        answer = modi() + " " + nouni()

        return answer

def nouni() :

    global nounnum
    
    a = nounnum % 11

    if a == 0 :
        a = 11

    nounnum += 1

    return noun[a-1]

def modi() :

    global modinum
    global adjectnum
    global adverbnum
    
    a = modinum % 2

    modinum += 1

    if a == 1 :
        return adject()
    elif a == 0 :
        answer = adve() + " " + adject()
        return answer

def adve() :

    global adverbnum
    
    a = adverbnum % 5

    if a == 0 :
        a = 5

    adverbnum += 1

    return adverb[a-1]

def adject() :

    global adjectnum
    
    a = adjectnum % 7

    if a == 0 :
        a = 7

    adjectnum += 1

    return adjective[a-1]

def pastrel() :

    global pastpnum
    global pastvnum
    
    a = pastpnum % 5
    b = pastvnum % 2

    if a == 0 :
        a = 5

    if b == 0 :
        b = 2
    
    answer = "Your " + pastp[a-1] + " " + pastv[b-1]

    pastpnum += 1
    pastvnum += 1
    
    return answer

def presentrel() :

    global prepnum
    global prevnum
    
    a = prepnum % 3
    b = prevnum % 2

    if a == 0 :
        a = 3

    if b == 0 :
        b = 2
    
    answer = "Your " + prep[a-1] + " " + prev[b-1]

    prepnum += 1
    prevnum += 1
    
    return answer

def childcheck(knight) :
    check = ["t","h","e","h","o","l","y","g","r","a","i","l"]

    now = 0

    for i in knight :
        if now < 12 :
            for j in range(len(i)) :
                if now < 12 :
                    if i[j] == check[now] :
                        now += 1
                else :
                    break
        else :
            break

    if now == 12 :
        return True
    else :
        return False    

while True :
    knight = list(map(str, input().split()))

    needcount = 0

    for i in knight :
        if i != "." :
            needcount += 1

    checkmok = needcount // 3
    checkleft = 1 if needcount % 3 != 0 else 0

    answercount = 0

    answercount += checkmok
    answercount += checkleft

    tauntcount = 0
    
    childgo = childcheck(knight)

    myanswer = []

    if childgo :
        tauntcount += 1
        myanswer.append("(A childish hand gesture).")

    while answercount > tauntcount :
        temptaunt = taunt()

        if "!" in temptaunt :
            tauntcount += 2
        else :
            tauntcount += 1

        myanswer.append(temptaunt)

    knightment = "Knight: "

    for i in knight :
        knightment += i
        knightment += " "

    print(knightment)

    for i in myanswer :
        tauntment = "Taunter: " + i
        print(tauntment)

    print("")
    
