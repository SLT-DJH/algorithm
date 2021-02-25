import math

class Node(object) :
    def __init__(self, key) :
        self.key = key
        self.child = {}
        self.check = False

class Trie(object) :
    def __init__(self) :
        self.head = Node(None)

    def insert(self, word) :
        curr = self.head

        for char in word :
            if char not in curr.child :
                curr.child[char] = Node(char)

            curr = curr.child[char]

        curr.child['*'] = True
        curr.check = True

    def search(self, word, visited) :

        temp = 1
        
        curr = self.head

        if curr not in visited :
            visited.append(curr)
            temp *= math.factorial(len(curr.child))

        for char in word :
            curr = curr.child[char]
            if curr not in visited :
                visited.append(curr)
                if len(curr.child) != 0 :
                    temp *= math.factorial(len(curr.child))
            
        return temp % 1000000007

N = int(input())

trie = Trie()

answer = 1

visited = []

box = []

for _ in range(N) :
    name = str(input())
    box.append(name)

box.sort()

for i in range(N) :
    if i == 0 :
       continue
    else :
        spell = ""
        for j in range(len(box[i])) :
            if j < len(box[i-1]) :
                if box[i-1][j] == box[i][j] :
                    spell += box[i][j]
                else :
                    spell += box[i][j]
                    break
            else :
                spell += box[i][j]
                break
        box[i] = spell

for i in box :
    trie.insert(i)

for i in box :
    answer *= trie.search(i, visited)

print(answer % 1000000007)
