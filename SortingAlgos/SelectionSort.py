class SelectionSort:
    def __init__(self,nums):
        self.nums = nums
        self.n = len(self.nums)

    def min_val(self,start_index):
        min_val_index = start_index
        for i in range(start_index+1,self.n):
            if self.nums[i] < self.nums[min_val_index]:
                min_val_index = i
        return min_val_index

    def sort(self):
        for i in range(self.n):
            index = self.min_val(i)
            self.nums[i] , self.nums[index] = self.nums[index],self.nums[i]
        print(self.nums)


if __name__ == "__main__":
    select_sort = SelectionSort([2,-1,-234,2])
    select_sort.sort()

