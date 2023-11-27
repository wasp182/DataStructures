
class HeapTransformer():
    def __init__(self,heap):
        self.heap = heap
        self.heap_size = len(heap)

    def max2min_heap(self):
        # start from internal nodes and swap them
        largest_internal = (len(self.heap)-2)//2
        for i in range(largest_internal,-1,-1):
            self.fix_down(i)

    # start with root node to ensure heap properties are maintained
    # O(Log N) running time complexity
    def fix_down(self,index):
        left_index = 2*index + 1
        right_index = 2*index + 2
        smallest_index = index

        # check if left or right child are smaller than index and store which index has the largest value
        if left_index < self.heap_size and self.heap[left_index] < self.heap[index]:
            smallest_index = left_index
        if right_index < self.heap_size and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index

        # if the index is the largest index compared to children then we can terminate the recursion
        if index != smallest_index:
            self.heap[index],self.heap[smallest_index] = self.heap[smallest_index],self.heap[index]
            self.fix_down(smallest_index)

if __name__ == "__main__":
    n = [210,100,23,2,5]
    heap_transform = HeapTransformer(n)
    heap_transform.max2min_heap()
    print(heap_transform.heap)
