import heapq

heap = [99, 8, 13, -2, 1, -5, 0, 0, 0, 0]
heapq.heapify(heap)

py_heap = []
# we can also create heaps in python
for items in heap:
    heapq.heappush(py_heap ,items)

print(py_heap)

# we can also pop out heap using heap sort
# below gives result of heap sort
while py_heap:
    print(heapq.heappop(py_heap))
