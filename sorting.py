from copy import deepcopy
from time import time
import random
import math
import matplotlib.pyplot as plt


def selection_sort(arr):

    selection_counter = 0

    for i in range(len(arr) - 1):
        minimal = arr[i]
        minimal_index = i
        for j in range(i, len(arr)):
            selection_counter += 1
            if arr[j] < minimal:
                minimal = arr[j]
                minimal_index = j
        arr[i], arr[minimal_index] = arr[minimal_index], arr[i]
    return arr, selection_counter


def insertion_sort(arr):

    insertion_counter = 0

    for i in range(1, len(arr)):
        index = 0
        pointer = 1
        while arr[i] <= arr[i - pointer]:
            insertion_counter += 1
            if pointer == i:
                break
            pointer += 1
        insertion_counter += 1
        index = i - pointer
        arr.insert(index + 1, arr.pop(i))
    return arr, insertion_counter


def merge_sort(arr):

    def merge_arrays(arr1, arr2):

        global merge_counter

        new_arr = []
        while len(arr1) > 0 and len(arr2) > 0:
            merge_counter += 1
            if arr1[0] < arr2[0]:
                new_arr.append(arr1.pop(0))
            else:
                new_arr.append(arr2.pop(0))
        if len(arr1) != 0:
            new_arr.extend(arr1)
        else:
            new_arr.extend(arr2)
        return new_arr
    
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def shell_sort(arr):

    shell_counter = 0 

    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j - gap] > temp:
                shell_counter += 1
                arr[j] = arr[j-gap]
                j -= gap
            shell_counter += 1
            arr[j] = temp
        gap //= 2
    return arr, shell_counter

def create_random_array(size: int):
    arr = []
    for _ in range(size):
        arr.append(random.random())
    return arr


def three_element_array(size: int):
    arr = []
    for _ in range(size):
        arr.append(random.randint(1, 3))
    return arr


def sorting_results(arr):

    global merge_counter

    counter_arr = []
    time_arr = []

    selection_copy = deepcopy(arr)
    insertion_copy = deepcopy(arr)
    merge_copy = deepcopy(arr)
    shell_copy = deepcopy(arr)

    start = time()
    selection_counter = selection_sort(selection_copy)[1]
    end = time()
    counter_arr.append(selection_counter)
    time_arr.append(end - start)

    start = time()
    insertion_counter = insertion_sort(insertion_copy)[1]
    end = time()
    counter_arr.append(insertion_counter)
    time_arr.append(end - start)

    start = time()
    merge_counter = 0
    merge_sort(merge_copy)
    end = time()
    counter_arr.append(merge_counter)
    time_arr.append(end - start)

    start = time()
    shell_counter = shell_sort(shell_copy)[1]
    end = time()
    counter_arr.append(shell_counter)
    time_arr.append(end - start)

    return counter_arr, time_arr


def results_random():

    selection_counter = []
    insertion_counter = []
    merge_counter = []
    shell_counter = []
    xlabels = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]

    for i in range(7, 16):

        time_sum = [0, 0, 0, 0]
        counter_sum = [0, 0, 0, 0]

        for _ in range(5):
            arr = create_random_array(2**i)
            results = sorting_results(arr)
            for j in range(4):
                counter_sum[j] += results[0][j]
                time_sum[j] += results[1][j]
        for j in range(4):
            counter_sum[j] /= 5
            time_sum[j] /= 5

        selection_counter.append(counter_sum[0])
        insertion_counter.append(counter_sum[1])
        merge_counter.append(counter_sum[2])
        shell_counter.append(counter_sum[3])

    plt.plot(xlabels, selection_counter, color = "red")
    plt.plot(xlabels, insertion_counter, color = "green")
    plt.plot(xlabels, merge_counter, color = "blue")
    plt.plot(xlabels, shell_counter, color = "yellow")
    plt.yscale('log')
    plt.xlabel("Size")
    plt.ylabel("Comperison count")
    plt.show()

    return


def results_sorted():

    selection_counter = []
    insertion_counter = []
    merge_counter = []
    shell_counter = []
    xlabels = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]

    for i in range(7, 16):

        time_sum = [0, 0, 0, 0]
        counter_sum = [0, 0, 0, 0]
        arr = create_random_array(2**i)
        shell_sort(arr)
        results = sorting_results(arr)

        for j in range(4):
            counter_sum[j] = results[0][j]
            time_sum[j] = results[1][j]

        selection_counter.append(counter_sum[0])
        insertion_counter.append(counter_sum[1])
        merge_counter.append(counter_sum[2])
        shell_counter.append(counter_sum[3])

    plt.plot(xlabels, selection_counter, color = "red")
    plt.plot(xlabels, insertion_counter, color = "green")
    plt.plot(xlabels, merge_counter, color = "blue")
    plt.plot(xlabels, shell_counter, color = "yellow")
    plt.yscale('log')
    plt.xlabel("Size")
    plt.ylabel("Comperison count")
    plt.show()

    return


def results_reverse():

    selection_counter = []
    insertion_counter = []
    merge_counter = []
    shell_counter = []
    xlabels = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]

    for i in range(7, 16):

        time_sum = [0, 0, 0, 0]
        counter_sum = [0, 0, 0, 0]
        arr = create_random_array(2**i)
        shell_sort(arr)
        arr = list(reversed(arr))
        results = sorting_results(arr)

        for j in range(4):
            counter_sum[j] = results[0][j]
            time_sum[j] = results[1][j]

        selection_counter.append(counter_sum[0])
        insertion_counter.append(counter_sum[1])
        merge_counter.append(counter_sum[2])
        shell_counter.append(counter_sum[3])

    plt.plot(xlabels, selection_counter, color = "red")
    plt.plot(xlabels, insertion_counter, color = "green")
    plt.plot(xlabels, merge_counter, color = "blue")
    plt.plot(xlabels, shell_counter, color = "yellow")
    plt.yscale('log')
    plt.xlabel("Size")
    plt.ylabel("Comperison count")
    plt.show()

    return


def results_three_element():

    selection_counter = []
    insertion_counter = []
    merge_counter = []
    shell_counter = []
    xlabels = ["2^7", "2^8", "2^9", "2^10", "2^11", "2^12", "2^13", "2^14", "2^15"]

    for i in range(7, 16):

        time_sum = [0, 0, 0, 0]
        counter_sum = [0, 0, 0, 0]

        for _ in range(3):
            arr = three_element_array(2**i)
            results = sorting_results(arr)
            for j in range(4):
                counter_sum[j] += results[0][j]
                time_sum[j] += results[1][j]
        for j in range(4):
            counter_sum[j] /= 5
            time_sum[j] /= 5

        selection_counter.append(counter_sum[0])
        insertion_counter.append(counter_sum[1])
        merge_counter.append(counter_sum[2])
        shell_counter.append(counter_sum[3])

    plt.plot(xlabels, selection_counter, color = "red")
    plt.plot(xlabels, insertion_counter, color = "green")
    plt.plot(xlabels, merge_counter, color = "blue")
    plt.plot(xlabels, shell_counter, color = "yellow")
    plt.yscale('log')
    plt.xlabel("Size")
    plt.ylabel("Comperison count")
    plt.show()

    return


results_random()
results_sorted()
results_reverse()
results_three_element()
