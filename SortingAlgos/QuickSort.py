class QuickSort():
    def __init__(self,nums):
        self.nums = nums

    def sort(self):
        self.quick_sort(0,len(self.nums)-1)
        # print(self.nums)

    def quick_sort(self,low,high):
        # print(low,high)
        if low >= high:
            return
        pivot = self.partition(low,high)
        # print(low,pivot,high)
        self.quick_sort(low,pivot-1)
        self.quick_sort(pivot+1,high)

    def partition(self,low,high):
        pivot = (low+high)//2
        # i /  low will reach till pivot value once below for loop is complete
        i = low
        self.nums[pivot] , self.nums[high] = self.nums[high] , self.nums[pivot]
        for j in range(low,high):
            if self.nums[j] <= self.nums[high]:
                self.nums[i] ,self.nums[j] = self.nums[j] , self.nums[i]
                i += 1
        # i will reach till value that all smaller values are less than pivot value in high position
        self.nums[high] , self.nums[i] = self.nums[i] , self.nums[high]
        return i

if __name__ == "__main__":
    qs = QuickSort([1,3,53,73,4,6,723,-3,2])
    qs.sort()









