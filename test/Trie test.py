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

        curr.check = True


    def search(self, word) :
        count = 0
        
        curr = self.head

        for char in word :
            curr = curr.child[char]
            if len(curr.child) > 1 or curr.check :
                count += 1

        return count

trie = Trie()
a = 'hello'
b = 'hell'
c = 'heaven'
d = 'goodbye'
trie.insert(a)
trie.insert(b)
trie.insert(c)
trie.insert(d)
