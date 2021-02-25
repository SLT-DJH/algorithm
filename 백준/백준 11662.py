Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())


def Minho(p) :
    global Ax
    global Bx
    global Ay
    global By

    return ((Ax + ((Bx-Ax) * (p /100))), (Ay + ((By-Ay) * (p /100))))

def Kangho(p) :
    global Cx
    global Dx
    global Cy
    global Dy

    return ((Cx + ((Dx-Cx) * (p /100))), (Cy + ((Dy-Cy) * (p /100))))


start = 0
end = 100
answer = 10000000000

while (end - start) >= 1e-6 :
    a = (start * 2 + end) / 3
    b = (start + end * 2) / 3

    aMinx, aMiny = Minho(a)
    bMinx, bMiny = Minho(b)

    aKangx, aKangy = Kangho(a)
    bKangx, bKangy = Kangho(b)

    aRange = (((aKangx - aMinx) ** 2) + ((aKangy - aMiny) ** 2)) ** 0.5
    bRange = (((bKangx - bMinx) ** 2) + ((bKangy - bMiny) ** 2)) ** 0.5

    answer = min(aRange, bRange)

    if aRange >= bRange :
        start = a
    else :
        end = b

print(answer)
