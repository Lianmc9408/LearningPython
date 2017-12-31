
import random


def select_sort1(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            # print(j)
            if array[i] > array[j]:
                # print('j', j)
                array[i], array[j] = array[j], array[i]


# 优化
def select_sort2(array):
    for i in range(len(array)):
        select_index = i
        for j in range(i, len(array)):
            if array[select_index] > array[j]:
                select_index = j
        array[i], array[select_index] = array[select_index], array[i]

import time
if __name__ == '__main__':
    array = []
    for i in range(10000):
        array.append(random.randint(0, 100000))
    print(array)
    start = time.time()
    select_sort1(array)
    end = time.time()
    print(end-start)
    print(array)