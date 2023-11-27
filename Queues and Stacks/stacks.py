class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack_size() >= 1 :
            data = self.stack[-1]
            del self.stack[-1]
            return data
        else:
            return -1

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)
