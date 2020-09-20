def cal(number, time, divide) :
    if time == 1 :
        d = number % divide
        return d
    if time % 2 == 0 :
        return (cal(number, time/2, divide) ** 2) % divide
    if time % 2 != 0 :
        return (cal(number, (time - 1)/2, divide) ** 2) * number % divide
    
a = input()

a = list(map(int, a.split()))


print(cal(a[0], a[1], a[2]))
