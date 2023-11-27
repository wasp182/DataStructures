class RadixSort:
    def __init__(self,data):
        self.data = data

    def get_digit(self):
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digit()):
            self.count_array_sort(digit)
        # print(self.data)

    def count_array_sort(self,d):
        # we add the number to [] inside the 2D array since we dont know how many items in data
        # array will be put in given digit bucket
        count_array = [[] for _ in range(10)]
        for item in self.data:
            # get the index for getting
            index = (item//(10**d)) % 10
            count_array[index].append(item)
        z = 0
        for i in range(len(count_array)):
            while len(count_array[i]) > 0 :
                # this means there is an item in this index
                self.data[z] = count_array[i].pop(0)
                # here pop method take O(N) running time complexity
                z += 1


if __name__ == "__main__":
    n = [123,13,53,34,3,43,5,74]
    rx = RadixSort(n)
    rx.sort()











