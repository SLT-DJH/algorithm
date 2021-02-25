while True :
    target = int(input())
    mlist = list(map(int, input().split()))

    count = 0

    def BS(array, target, start, end) :
        global count

        if start >= end :
            return
        
        mid = (start + end) // 2

        middle = array[mid]
        
        if target == middle  :
            count += 1
            midminus = mid
            midplus = mid
            while True :
                midminus -= 1
                if array[midminus] == target :
                    count += 1
                    if midminus == 0 :
                        break
                else :
                    break

            while True :
                midplus += 1
                if array[midplus] == target :
                    count += 1
                    if midplus == len(array) - 1 :
                        break
                else :
                    break

            return
        elif middle > target :
            BS(array, target, start, mid - 1)
        elif middle < target :
            BS(array, target, mid + 1, end)

    mlist.sort()

    start = 0
    end = len(mlist) - 1

    BS(mlist, target, start, end)

    print(count)
