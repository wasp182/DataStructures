import random
import statistics

import QuickSort as q
import RadixSort as c
import time

n = [n for n in range(10000)]
quickTime = []
radixTime = []

for _ in range(100):

    random.shuffle(n)
    sort1 = q.QuickSort(n)
    t = time.time()
    sort1.sort()
    quickTime.append(time.time()-t)
print('Average Quicksort time taken: %s' % str(statistics.mean(quickTime)))

for _ in range(100):
    random.shuffle(n)
    sort2 = c.RadixSort(n)
    t = time.time()
    sort2.sort()
    radixTime.append(time.time()-t)
print('Average Radix sort time taken: %s' % str(statistics.mean(radixTime)))

