def shell_sort(nums):
    gap = len(nums)//2
    while gap > 0:
        for i in range(gap,len(nums)):
            j = i
            while j > 0 and nums[j-gap] > nums[j] :
                nums[j-gap] , nums[j] = nums[j] , nums[j-gap]
                j = j - gap
        gap = gap // 2
    print(nums)

if __name__ == "__main__":
    shell_sort([23,64,3,71,45,74,2,5,3,32])

