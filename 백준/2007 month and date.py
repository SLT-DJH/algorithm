a = input()
a = a.split()
b = []
b.append(int(a[0]))
b.append(int(a[1]))


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

month = b[0]
day = b[1]

totaldays = 0

minimonth = 1

while minimonth < month :
    totaldays = totaldays + days[minimonth - 1]
    minimonth = minimonth + 1

totaldays = totaldays + day

print(date[totaldays % 7])
