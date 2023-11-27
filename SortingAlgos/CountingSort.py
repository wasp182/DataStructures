class SortingAlgorithm:
    def __init__(self,data):
        self.data = data
        self.count_array = [0 for _ in range(max(data)-min(data)+1)]
        # self.k = len(self.count_array)

    def sort(self):
        for i in range(len(self.data)):
            self.count_array[self.data[i]-min(self.data)] += 1

        # enumerate the count array
        z = 0
        for i in range(min(self.data),max(self.data)+1):
            while self.count_array[i-min(self.data)] > 0 :
                self.data[z] = i
                z += 1
                self.count_array[i-min(self.data)] -= 1
        print(self.data)

if __name__ == "__main__":
    n = [123,23,6,462,466,53,34,2,865,34]
    s1 = SortingAlgorithm(n)
    s1.sort()



