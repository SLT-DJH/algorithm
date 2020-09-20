def search(number, inputlist) :
    inputlist.sort()
    mini = 0
    maxi = len(inputlist) - 1
    mid = (mini + maxi) // 2
    if number == inputlist[mid] :
        return True
    else :
        while mini < mid :
            if number > inputlist[mid] :
                mini = mid
                mid = (mini + maxi) // 2
            elif number < inputlist[mid] :
                maxi = mid
                mid = (mini + maxi) // 2
            else :
                break
        if inputlist[mini] == number or inputlist[maxi] == number or inputlist[mid] == number:
            return True
        else :
            return False
    

N = int(input())

sangcard = input()
sangcard = list(map(int, sangcard.split()))

M = int(input())

whatcard = input()
whatcard = list(map(int,whatcard.split()))

answer = ''

for i in range(M) :
    if search(whatcard[i], sangcard) :
        answer = answer + '1 '
    else :
        answer = answer + '0 '

print(answer)

