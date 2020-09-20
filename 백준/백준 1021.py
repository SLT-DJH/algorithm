from collections import deque

a = input()
b = input()

a = list(map(int, a.split()))
b = list(map(int, b.split()))

n = a[0]

countsum = 0

getlist = []
numlist = deque([])

for i in range(n) :
    getlist.append(i+1)

for i in b :
    numlist.append(i)

while True :
    check = numlist[0]

    leftindex = getlist.index(check)
    rightindex = len(getlist) - leftindex

    if leftindex == 0 :
        getlist = getlist[1:]
        numlist.popleft()
    elif leftindex == len(getlist) - 1 :
        countsum += 1
        getlist = getlist[:leftindex]
        numlist.popleft()
    else :
        if leftindex < rightindex :
            countsum += leftindex
            basic = getlist[leftindex+1:]
            new = getlist[:leftindex]
            getlist = basic + new
            numlist.popleft()
        else :
            countsum += rightindex
            basic = getlist[:leftindex]
            new = getlist[leftindex+1:]
            getlist = new + basic
            numlist.popleft()

    if numlist == deque([]) :
        break

print(countsum)

    

