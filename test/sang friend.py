N = int(input())

M = int(input())

sangfriend = []
friendfriend = []
mylist = []

for i in range(M) :
    find = input()
    find = list(map(int, find.split()))
    if find[0] == 1 :
        sangfriend.append(find[1])
    elif find[1] == 1 :
        sangfriend.append(find[0])
    mylist.append(find)

for i in range(M) :
    find = mylist[i]
    if find[0] in sangfriend :
        friendfriend.append(find[1])
    elif find[1] in sangfriend :
        friendfriend.append(find[0])

sangfriend = set(sangfriend)
friendfriend = set(friendfriend)
        

print(len(sangfriend | friendfriend) - 1)
    
