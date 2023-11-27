from collections import deque


class QuickSortIterative:

    def __init__(self, data):
        self.data = data

    def partition(self, low, high):

        pivot_index = (low + high) // 2
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for j in range(low, high, 1):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low = low + 1

        self.data[low], self.data[high] = self.data[high], self.data[low]

        return low

    def sort(self):

        # stack implementation with a doubly linked list
        # recursion uses the stack memory of the OS
        # now we create a stack on our own !!!
        stack = deque()

        # start index and end index
        stack.append((0, len(self.data)-1))

        # while stack is not empty
        while stack:

            start, end = stack.pop()
            # PARTITION PHASE
            pivot = self.partition(start, end)

            # CONQUER PHASE but not with recursion - we manually push the indexes onto the stack
            # considering the left sub-array
            if pivot - 1 > start:
                stack.append((start, pivot - 1))

            # considering the right sub-array
            if pivot + 1 < end:
                stack.append((pivot + 1, end))


if __name__ == '__main__':

    n = [5, 4, 3, 2, 1]
    sort = QuickSortIterative(n)
    sort.sort()
    print(sort.data)