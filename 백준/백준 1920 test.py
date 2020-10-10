def search(num, nlist) :
    start = 0
    end = len(nlist) - 1
    mid = (start + end) // 2

    while mid != start and mid != end :
        if nlist[mid] == num :
            return 1
        else :
            if nlist[mid] > num :
                end = mid
                mid = (start + end) // 2
            else :
                start = mid
                mid = (start + end) // 2

    if nlist[mid] == num :
        return 1
    elif mid+1 <= len(nlist)-1 and nlist[mid+1] == num:
        return 1
    elif mid-1 >= 0 and nlist[mid-1] == num :
        return 1

    return 0


nlist = [-300, -252, -35, -145, - 24, 0, 25, 256, 5156, 23, 2, 14, 26, 87, -789, 13, 61]

nlist.sort()

print(nlist)

num = int(input())

print(search(num, nlist))
