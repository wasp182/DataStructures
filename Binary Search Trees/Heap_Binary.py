CAPACITY = 10
class Heap:
    def __init__(self):
        self.heap_size = 0
        self.heap = [0]*CAPACITY

    def insert(self,item):
        # heap is full
        if self.heap_size == CAPACITY:
           return
        self.heap[self.heap_size] = item
        self.heap_size += 1
        # Check Heap properties for given index of heap
        self.fix_up(self.heap_size-1)

    # starting with actual node we have inserted upto root node
    # log(n) comparisons to be done to compare values and swap
    def fix_up(self,index):
            parent_index = (index-1)//2
            if index > 0 and self.heap[parent_index] < self.heap[index]:
                # swap the items and check recursively till root node
                self.heap[parent_index] , self.heap[index] = self.heap[index] , self.heap[parent_index]
                self.fix_up(parent_index)

    # peek returns max item in heap
    def get_max(self):
        return self.heap[0]

    # return max and remove it as well
    def poll(self):
        max_item = self.get_max()
        self.heap[0] , self.heap[self.heap_size-1] = self.heap[self.heap_size-1] , self.heap[0]
        self.heap_size -= 1

        # check for violation of heap properties from root node onward
        self.fix_down(0)

        return max_item

    # start with root node to ensure heap properties are maintained
    # O(Log N) running time complexity
    def fix_down(self,index):
        left_index = 2*index + 1
        right_index = 2*index + 2
        largest_index = index

        # check if left or right child are smaller than index and store which index has the largest value
        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # if the index is the largest index compared to children then we can terminate the recursion
        if index != largest_index:
            self.heap[index],self.heap[largest_index] = self.heap[largest_index],self.heap[index]
            self.fix_down(largest_index)

    def heap_sort(self):
        # heap sort will take the root item each time from heap and fix down
        # this takes O(N) runing time to parse through all items and Log(N) time
        # for checking heap properties
        # O(N*Log N) running time complexity , this is guaranteed runing time
        # unlike quick sort
        for _ in range(self.heap_size):
            max_item = self.poll()
            print(max_item)

if __name__ == "__main__":
    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)
    print(heap.heap)
    heap.heap_sort()