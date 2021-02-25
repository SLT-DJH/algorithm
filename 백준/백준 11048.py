import sys

def check(num, numlist, mid, N) :
    numcount = 0
    for i in range(mid) :
        if numlist[i] == num :
            numcount += 1
        else :
            break
    
    for i in range(mid+1, N) :
        if numlist[i] == num :
            numcount += 1
        else :
            break
    return numcount + 1

def find(num, numlist, start, end, count) :
    if start > end :
        return
    else :
        mid = (start + end) // 2
        
        if numlist[mid] == num :
            count.append(check(num, numlist, mid, N))
            return
        elif numlist[mid] > num :
            find(num, numlist, start, mid-1, count)
        elif numlist[mid] < num :
            find(num, numlist, mid+1, end, count)

N = int(input())
numlist = list(map(int, input().split()))
M = int(input())
checklist = list(map(int, input().split()))

numlist.sort()

count = []

for i in checklist :
    find(i, numlist, 0, N-1, count)
    
answer = ""

for i in count :
    answer += str(i)
    answer += " "

print(answer)
