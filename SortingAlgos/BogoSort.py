import random

class BogoSort:
    def __init__(self,nums):
        self.nums = nums

    def is_sorted(self):
        for i in range(1,len(self.nums)):
            if self.nums[i-1] >  self.nums[i]:
                return False
        return True

    def sort(self):
        while not self.is_sorted():
            print("shuffle")
            self.shuffle()
        print("Final Sorted List:")
        print(self.nums)

    def shuffle(self):
        for i in range(len(self.nums)-1,0,-1):
            j = random.randrange(0,i+1)
            temp=self.nums[i]
            self.nums[i] = self.nums[j]
            self.nums[j] = temp
        print(self.nums)

if __name__ == "__main__":
    s1 = BogoSort([56,7])
    # sorting.shuffle()
    s1.sort()
