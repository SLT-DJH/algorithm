class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):

        if self.stack != [] :
            self.stack.pop()
        

    def top(self):

        if self.stack == [] :
            return None
        else :
            return self.stack[len(self.stack) - 1]

    def getMin(self):

        return min(self.stack)
