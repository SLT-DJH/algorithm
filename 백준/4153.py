while True :
    case = input()

    case = list(map(int, case.split()))

    x = max(case)

    case.remove(max(case))

    y = case[0]

    z = case[1]

    if x == 0 and y == 0 and z == 0 :
        break
    else :
        if x ** 2 == y ** 2 + z ** 2 :
            print("right")
        else :
            print("wrong")
        
