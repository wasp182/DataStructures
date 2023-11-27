# The aim is to design a queue abstract data type with the help of stacks.
from stacks import Stack

class QueueWithStacks():
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueque(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0 :
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

if __name__ == "__main__":
    queue = QueueWithStacks()
    queue.enqueque(55)
    queue.enqueque(56)
    queue.enqueque(57)
    print(queue.dequeue())
    print(queue.dequeue())



