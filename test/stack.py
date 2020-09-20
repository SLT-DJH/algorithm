class stack :
    def __init__(self) :
        self.items = []
    def push(self, item) :
        self.items.append(item)
    def pop(self) :
        if len(self.items) == 0 :
            return -1
        else :
            return self.items.pop()
    def size(self) :
        return len(self.items)
    def empty(self) :
        if len(self.items) == 0 :
            return 1
        else :
            return 0
    def top(self) :
        if len(self.items) == 0 :
            return -1
        else :
            return self.items[len(self.items) - 1]



N = int(input())

answer = []

box = stack()

for i in range(N) :
    b = input()
    b = b.split()
    check = b[0]
    if check == 'push' :
        box.push(int(b[1]))
    elif check == 'pop' :
        answer.append(box.pop())
    elif check == 'size' :
        answer.append(box.size())
    elif check == 'empty' :
        answer.append(box.empty())
    elif check == 'top' :
        answer.append(box.top())

for i in range(len(answer)) :
    print(answer[i])
