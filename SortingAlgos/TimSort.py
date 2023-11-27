import random


class TimSort:

    def __init__(self, data):
        self.data = data

    def sort(self):
        self.merge_sort(self.data)

    # it is the exact same merge sort we have implemented together except for the base case
    def merge_sort(self, nums):

        # this is where the magic happens: the original merge sort returns when there is just a single item
        # in the subarray. Here we have to switch to insertion sort when the number of items
        # is relatively small (64 in the original implementation)
        if len(nums) <= 64:
            self.insertion_sort(nums)
            return

        # DIVIDE PHASE
        middle_index = len(nums) // 2
        left_half = nums[:middle_index]
        right_half = nums[middle_index:]

        self.merge_sort(left_half)
        self.merge_sort(right_half)

        # CONQUER PHASE
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i = i + 1
            else:
                nums[k] = right_half[j]
                j = j + 1

            k = k + 1

        # after that there may be additional items in the left (right) sub-array
        while i < len(left_half):
            nums[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j = j + 1
            k = k + 1

    # it is the exact same insertion sort we have implemented together
    def insertion_sort(self, sub_array):

        for i in range(len(sub_array)):

            j = i

            while j > 0 and sub_array[j - 1] > sub_array[j]:
                sub_array[j], sub_array[j - 1] = sub_array[j - 1], sub_array[j]
                j = j - 1


if __name__ == "__main__":

    n = [n for n in range(100000)]
    random.shuffle(n)
    sort = TimSort(n)
    sort.sort()
    print(sort.data)