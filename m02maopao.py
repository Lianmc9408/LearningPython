
import random

if __name__ == '__main__':
    array = []
    for i in range(50):
        array.append(random.randint(0, 1000))
    print(array)
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    print(array)
