class QueueWithRecursion():
    def __init__(self):
        self.enqueue_stack = []

    def enqueque(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack)==1:
            return self.enqueue_stack.pop()
        # pop item fo next call
        item = self.enqueue_stack.pop()
        dequeued_item = self.dequeue()
        # we have got the first item in list
        self.enqueue_stack.append(item)
        return dequeued_item


if __name__ == "__main__":
    queue = QueueWithRecursion()
    queue.enqueque(55)
    queue.enqueque(56)
    queue.enqueque(57)
    print(queue.dequeue())
    print(queue.dequeue())