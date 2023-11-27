import random

# this approach requires extra memory
import timeit


def dutch_sort(list_dutch):
    l = len(list_dutch)
    zeros , ones , twos = 0 , 0, 0
    for i in range(l):
        if list_dutch[i] == 0:
            zeros += 1
        elif list_dutch[i] == 1:
            ones += 1
        elif list_dutch[i] == 2 :
            twos += 1
    index = 0
    while index < l :
        if ones + zeros + twos == l :
            if index < zeros:
                list_dutch[index] = 0
            elif zeros <= index < zeros+ones:
                list_dutch[index] = 1
            else: list_dutch[index] = 2
        index +=1
    print(list_dutch)


def dutch_sort_partition(list_dutch):
    i ,j , k = 0 , 0, len(list_dutch)-1
    while j <= k:
        if list_dutch[j] < 1:
            list_dutch[i] , list_dutch[j] = list_dutch[j] , list_dutch[i]
            i += 1
            j += 1
        elif list_dutch[j] > 1 :
            list_dutch[k] , list_dutch[j] = list_dutch[j] , list_dutch[k]
            k -= 1
        else: j += 1
    print(list_dutch)


if __name__ == "__main__":
    # testlist1 = """\
    test_list=[]
    for i in range(10):
        test_list.append(random.randint(0,2))
    print(test_list)
    dutch_sort(test_list)
    # """

    # testlist2="""\
    test_list2=[]
    for i in range(10):
        test_list2.append(random.randint(0,2))
    print(test_list2)
    dutch_sort_partition(test_list2)
    # """
    # def calls():


    res1 = timeit.repeat(stmt="dutch_sort(test_list)",globals=globals(),repeat=5,number=100)
    res2 = timeit.repeat(stmt="dutch_sort_partition(test_list2)",globals=globals(),repeat=5,number=100)
    print(res1)
    print(res2)