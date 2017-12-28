
import random


def select_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            print(j)
            if array[i] > array[j]:
                print('j', j)
                array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    array = []
    for i in range(50):
        array.append(random.randint(0, 1000))
    print(array)
    select_sort(array)
    print(array)