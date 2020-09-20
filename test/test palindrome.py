alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = "race a car"

s = s.lower()

box = []
rebox = []

for i in s :
    if i in alpha :
        box.append(i)
        rebox.append(i)

rebox.reverse()
