import random


def quick_sort(array, start, end):
    if start >= end:
        return
    k = array[start]
    left = start
    right = end
    while left < right:
        while left < right and array[right] > k:
            right -= 1
        array[left], array[right] = array[right], array[left]

        while left < right and array[left] <= k:
            left += 1
        array[left], array[right] = array[right], array[left]

    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


import time

if __name__ == '__main__':
    array = []
    for i in range(10):
        array.append(random.randint(0, 100))
    print(array)
    start = time.time()
    quick_sort(array, 0, len(array)-1)
    end = time.time()
    # print(end - start)
    print(array)
