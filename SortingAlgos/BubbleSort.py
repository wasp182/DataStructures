def bubble_sort(nums):
    n = len(nums)-1
    while n > 0:
        for i in range(n):
            if nums[i] > nums[i+1]:
                nums[i+1],nums[i] = nums[i],nums[i+1]
            else:
                continue
        n -= 1
    return nums

if __name__ == "__main__":
    print(bubble_sort([1,22,-32,4,345,1,23,11,2]))


