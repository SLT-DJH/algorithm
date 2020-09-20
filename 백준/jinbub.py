alphabet = {}

for i in range(26) :
    alphabet[chr(i + 65)] = i + 10

number = {}

for i in range(10) :
    number[chr(i+48)] = i

a = input()
a = a.split()

box = []

for i in range(len(a[0])) :
    box.append(a[0][i])

a[0] = box
a[1] = int(a[1])

total = 0

for i in range(len(a[0])) :
    if a[0][i] in alphabet :
        total = total + (alphabet[a[0][i]] * (a[1] ** (len(a[0]) - (i+1))))
    else :
        total = total + (number[a[0][i]] * (a[1] ** (len(a[0]) - (i+1))))
print(total)
