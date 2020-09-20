a = input()

a = list(map(int, a.split()))

x = a[0]

y = a[1]

w = a[2]

h = a[3]

possible = [h - y, w - x, y, x]

print(min(possible))
