class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    # O(1) running time
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.size_queque() != 0 :

            data = self.queue[0]
            # this is O(N) running time as it requires shifting the items in data structure
            del self.queue[0]
            return data
        else:
            return -1

    def peek(self):
        return self.queue[0]

    def size_queque(self):
        return len(self.queue)









