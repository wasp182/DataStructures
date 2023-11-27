import random
import csv
counter = 1

def insertion_sort(nums,n):
    global counter
    for i in range(1,len(nums)):
        index = i
        while nums[index] < nums[index-1] and index >= 1:
            nums[index-1] , nums[index] = nums[index] , nums[index-1]
            counter += 1
            index -= 1
    print(nums)
    with open("test_insertion_sort.csv",'a',newline="") as streams:
        obj = csv.writer(streams)
        obj.writerow([n,counter])


def insertion_sort_v2(nums):
    for i in range(1,len(nums)):
        index = i
        temp = nums[i]
        print(f"sn {i} , value :  {temp}")
        while True:
            if temp < nums[index-1] and index > 0 :
                nums[index] = nums[index-1]
                index -= 1
                print(nums)
            else:
                print()
                if index != i:
                    nums[index] = temp
                print(nums)
                break
    print(nums)


# start from beginning and keep iterating till we find place for given item to fit

if __name__ == "__main__":
    # insertion_sort([23,64,3,71,45,74,2,5,3,32])
    # insertion_sort_v2([23,64,3,71,45,74,2,5,3,32])
    for i in range(1,101):
        # l = [1,24,54,2765,436,63,6,-12,243,-5,-22,34,265,443,53,22,4766,337,67,41]
        l = [random.randint(1,100000) for _ in range(10*i)]
        # print(l)
        insertion_sort(l,len(l))

