# The aim is to design an algorithm that can return the maximum item of
# a stack in O(1) running time complexity. We can use O(N) extra memory!

from stacks import Stack

class MaxStack():
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self,data):
        self.main_stack.append(data)
        if len(self.main_stack) == 1 :
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1] :
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    def get_max_item(self):
        return self.max_stack.pop()




