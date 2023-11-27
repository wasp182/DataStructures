import random

def maximum(list):
    max = -1
    for item in list:
        if item > max:
            max = item
    return max


def left_right_max(data_list):
    i=1
    Leftlist = []
    Rightlist = []
    N = len(data_list)
    while i < N-1:
        # print(max([z for z in blocks_list[:i]]))
        maxLeft = maximum(z for z in data_list[0:i])
        maxRight = maximum(z for z in data_list[i + 1:])
        Leftlist.append(maxLeft)
        Rightlist.append(maxRight)
        i+=1
    return Leftlist,Rightlist


def rain_water(blocklist):
    left_max , right_max = left_right_max(blocklist)
    height , area ,i = 0 , 0 , 1
    N = len(blocklist)
    print(left_max)
    print(right_max)
    for i in range(1,N-1):
        height = min(left_max[i-1],right_max[i-1])-blocklist[i]
        if height > 0 :
            area += height
        i += 1
    print(area)
    return area


def rain_water_optimal(blocklist : list):
    N = len(blocklist)
    area = 0
    left_max = [0 for _ in range(N)]
    right_max = [0 for _ in range(N)]
    for i in range(1,N):
        left_max[i] = max(left_max[i-1],blocklist[i-1])
    for i in range(N-2,-1,-1):
        right_max[i] = max(right_max[i+1],blocklist[i+1])
    print(left_max)
    print(right_max)
    for i in range(1,N-1):
        height = min(left_max[i],right_max[i])-blocklist[i]
        if height > 0 :
            area += height
    print(area)
    return area

if __name__ == "__main__":
    # test_list=[]
    # for i in range(10):
    #     test_list.append(random.randint(0,12))
    # print(test_list)
    rain_water([5,1, 0, 2, 1, 3, 1, 2, 0, 3,9])
    rain_water_optimal([5,1, 0, 2, 1, 3, 1, 2, 0, 3,9])

