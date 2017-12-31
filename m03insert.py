import random


def insert_sort(array):
    for i in range(1, len(array)):
        position = i
        temp = array[i]
        while position > 0 and temp < array[position-1]:
            array[position] = array[position-1]
            position -= 1
        array[position] = temp

# 二分查找
def half(array, val):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if val > array[mid]:
            low = mid + 1
        elif val < array[mid]:
            high = mid - 1
        else:
            return mid
    return None


import time

if __name__ == '__main__':
    array = []
    for i in range(20):
        array.append(random.randint(0, 100))
    print(array)
    start = time.time()
    insert_sort(array)
    end = time.time()
    print(end - start)
    print(array)
