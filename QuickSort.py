
class QuickSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        self.quick_sort(0, len(self.data)-1)

    # low is the index of the first item
    # high is the index of the last item
    def quick_sort(self, low, high):

        if low >= high:
            return

        pivot_index = self.partition(low, high)
        # call the function recursively on the left array
        # we make (if the pivot selection is working fine) log2 function calls
        # MASTER THEOREM T(n) = 2 log + O(n) = O(NlogN)
        self.quick_sort(low, pivot_index - 1)
        # call the function recursively on the right array
        self.quick_sort(pivot_index + 1, high)

    # this is where the magic happens !!!
    # in O(N) linear running time complexity
    def partition(self, low, high):

        # we use the middle item as the pivot
        pivot_index = (low + high) // 2

        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        # consider all the other items and compare them with the pivot
        for j in range(low, high):
            if self.data[j] <= self.data[high]:
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low = low + 1

        # we have considered all the items - we have to swap the pivot and the low
        self.data[low], self.data[high] = self.data[high], self.data[low]

        # return the index of the pivot
        return low


if __name__ == '__main__':

    x = [1, -4, 0, 10, 5, 4, 3, 100]

    algorithm = QuickSort(x)
    algorithm.sort()
    print(x)
