# We have seen how to implement min (and max) heaps from scratch.
# Your task is to check whether a list contains a valid min heap or not.
#
# def is_min_heap(heap):
#     ...
#
# The heap is a list data structure containing integers.

def is_min_heap(heap):
    heap_size = len(heap)
    for i in range((heap_size-2)//2):
        left_index = 2*i + 1
        right_index = 2*i + 2
        if heap[i] > min(heap[left_index],heap[right_index]):
            return False
    return True

if __name__ == "__main__":
    n = [1,2,3,4,5]
    print(is_min_heap(n))
