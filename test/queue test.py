def Queue(queueList, queueCountList, number) :
    maxqueue = max(queueList)
    answer = 0
    count = 0
    while len(queueList) != 0 :
        if queueList[0] < maxqueue :
            queueList.insert(len(queueList), queueList[0])
            queueCountList.insert(len(queueCountList), queueCountList[0])
            queueList.remove(queueList[0])
            queueCountList.remove(queueCountList[0])
        elif queueList[0] >= maxqueue :
            queueList.remove(queueList[0])
            if queueCountList[0] == number :
                count = count + 1
                answer = count
                queueList = []
                break
            queueCountList.remove(queueCountList[0])
            count = count + 1
            if queueList == [] :
                continue
            else :
                maxqueue = max(queueList)
    print(answer)
                

a = input()
a = list(map(int, a.split()))
N = a[0]
M = a[1]

queue = input()
queue = list(map(int, queue.split()))

queueCount = []

for i in range(a[0]) :
    queueCount.append(i)

maxqueue = max(queue)

Queue(queue, queueCount, a[1])
