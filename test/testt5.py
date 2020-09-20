maxnumber = 20000000

box = []

for i in range(maxnumber) :
    box.append(0)

N = int(input())
sangnumber = input()
sangnumber = list(map(int, sangnumber.split()))

M = int(input())
whatnumber = input()
whatnumber = list(map(int, whatnumber.split()))

for i in range(N) :
    box[sangnumber[i] + 10000000] = 1

answer = ''

for i in range(M) :
    answer = answer + str(box[whatnumber[i] + 10000000]) + ' '

print(answer)
