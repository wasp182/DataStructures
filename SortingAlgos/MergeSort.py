import csv
import random

counter = 0

def merge_sort(nums,n=1):

    global counter
    if len(nums) == 1:
        return

    # divide approach
    middle_index = len(nums)//2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]
    # print("*"*40+"Dividing"+"*"*40)
    # print(left_half)
    # print(right_half)
    counter += 1

    merge_sort(left_half)
    merge_sort(right_half)

    # conquer approach
    index = 0
    i , j = 0, 0
    # this should take O(N) time
    while i < len(left_half) and j < len(right_half):
        if right_half[j] > left_half[i]:
            nums[index] = left_half[i]
            i += 1
        else:
            nums[index] = right_half[j]
            j += 1
        index += 1

    # in case one of the arrays is already filled in the nums array then we can move other array right to
    # the remaining part of nums array
    while i < len(left_half):
        nums[index] = left_half[i]
        i += 1
        index += 1
    while j < len(right_half):
        nums[index] = right_half[j]
        j += 1
        index += 1
    # print("*"*40+"Merging"+"*"*40)
    # print(nums)

    counter+=1
    if i+j == n:
         with open("test_sort.csv",'a',newline="") as streams:
            obj = csv.writer(streams)
            obj.writerow([n,counter])

if __name__ == "__main__":
    for i in range(1,101):
    # l = [1,24,54,2765,436,63,6,-12,243,-5,-22,34,265,443,53,22,4766,337,67,41]
        l = [random.randint(1,100000) for _ in range(10*i)]
        # print(l)
        merge_sort(l,len(l))
