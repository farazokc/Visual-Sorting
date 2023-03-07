import random
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
import tkinter


def swap(array, i, j):
    if i != j:
        array[i], array[j] = array[j], array[i]


def Bubblesort(array):
    n = len(array)

    if n == 1:
        return

    flag = True

    for i in range(n - 1):
        if not flag:
            break
        flag = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                flag = True
            yield array


def Mergesort(array, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from Mergesort(array, start, mid)
    yield from Mergesort(array, mid + 1, end)
    yield from merge(array, start, mid, end)
    yield array


def merge(array, start, mid, end):
    merged = []
    leftindex = start
    rightindex = mid + 1

    while leftindex <= mid and rightindex <= end:
        if array[leftindex] < array[rightindex]:
            merged.append(array[leftindex])
            leftindex += 1
        else:
            merged.append(array[rightindex])
            rightindex += 1

    while leftindex <= mid:
        merged.append(array[leftindex])
        leftindex += 1

    while rightindex <= mid:
        merged.append(array[rightindex])
        rightindex += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array


def QuickPartition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def Quicksort(array, low, high):
    if low < high:
        pi = QuickPartition(array, low, high)

        yield from Quicksort(array, low, pi - 1)
        yield from Quicksort(array, pi + 1, high)
        yield array


def heapify(array, element, i):
    high = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < element and array[i] < array[left]:
        high = left
    if right < element and array[high] < array[right]:
        high = right

    swap(array, i, high)
    if high != i:
        # array[i], array[high] = array[high], array[i]
        heapify(array, element, high)


def Heapsort(array):
    for i in range(element // 2 - 1, -1, -1):
        heapify(array, element, i)

    for i in range(element - 1, 0, -1):
        swap(array, i, 0)
        # array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        yield array


def Bucketsort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_bucket = 0
        bucket[index_bucket].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
            yield array


def Countingsort(array):
    maximum = int(max(array))
    minimum = int(min(array))
    range_max_min = maximum - minimum + 1

    count_array = [0 for _ in range(range_max_min)]
    out_array = [0 for _ in range(element)]

    for i in range(0, element):
        count_array[array[i] - minimum] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    for i in range(element - 1, -1, -1):
        out_array[count_array[array[i] - minimum] - 1] = array[i]
        count_array[array[i] - minimum] -= 1
        yield out_array
    # for i in range(0, element):
    #     array[i] = out_array[i]
    # yield array


def RadixCountingsort(array, exp1):
    output_array = [0] * (element)
    count_array = [0] * (10)

    for i in range(0, element):
        index = array[i] / exp1
        count_array[int(index % 10)] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    i = element - 1
    while i > 0:
        index = array[i] / exp1
        output_array[count_array[int(index % 10)] - 1] = array[i]
        count_array[int(index % 10)] -= 1
        i -= 1
        # yield count_array

    i = 0
    for i in range(0, len(array)):
        array[i] = output_array[i]
        # prev_arr = array[i]
        yield array

    # prev_arr = array[i]
    yield array


def Radixsort(array):
    # global prev_arr
    # prev_arr = [array[i] for i in range(len(array))]
    max1 = max(array)
    max_exp = len(str(abs(max1)))
    exp = 1
    pass_counter = 0

    while max1 / exp > 0:
        pass_counter += 1

        if pass_counter > max_exp:
            break
        yield from RadixCountingsort(array, exp)

        exp = exp * 10

        # print(prev_arr)
        # if np.array_equal(np.asarray(array), np.asarray(prev_arr)):
        # break
        # else:
        #     yield from RadixCountingsort(array, exp)

        # output_array = [0] * (element)
        # count_array = [0] * (10)

        # for i in range(0, element):
        #     index = array[i] / exp
        #     count_array[int(index % 10)] += 1

        # for i in range(1, 10):
        #     count_array[i] += count_array[i - 1]

        # i = element - 1
        # while i > 0:
        #     index = array[i] / exp
        #     output_array[count_array[int(index % 10)] - 1] = array[i]
        #     count_array[int(index % 10)] -= 1
        #     i -= 1

        # i = 0
        # for i in range(0, len(array)):
        #     array[i] = output_array[i]
        #     yield array
        #     # if np.any(np.asarray(array) != np.asarray(output_array)):
        #     #     yield array
        #     # else:
        #     #     pass_counter += 1
        #     #     if pass_counter > 5:
        #     #         # time.sleep(3)
        #     #         # sys.exit(2)
        #     #         return
        #     continue

    # yield array


def Insertionsort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
            yield array


def insertion_sort(arr, low, n):
    # print("Performing insertion sort...")
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val

    yield arr


def partition(arr, low, high):
    # print("Creating partition...")
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


def quick_sort(arr, low, high):
    # print("Starting quick sort routine")
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        return arr


# def to_stack(arr):
#     global pile
#     pile = [0] * len(arr)

#     if not np.array_equal(arr, pile[-1]):
#         print("Array stacked")
#         pile = np.vstack((pile, array))
#         # print(pile)
#     else:
#         print("Not stacked")


def quick_insertion_sort(arr, low, high):
    counter = 0

    while low < high:

        if high - low + 1 < 10:
            yield from insertion_sort(arr, low, high)
            # to_stack(arr)
            # yield arr
            break

        else:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                yield from quick_insertion_sort(arr, low, pivot - 1)
                low = pivot + 1
                # to_stack(arr)
            else:
                yield from quick_insertion_sort(arr, pivot + 1, high)
                high = pivot - 1
                to_stack(arr)

    yield arr


def preprocessing(arr, a, b):
    k = max(arr)
    nums = 0

    if b > k:
        b = k

    if a < 1:
        a = 1

    B = [0] * (k + 1)
    C = [0] * (k + 1)

    for count in range(len(arr)):
        B[arr[count]] += 1

    C[1] = B[1]

    for count in range(2, k + 1):
        C[count] = B[count] + C[count - 1]

    nums = C[b] - C[a] + B[a]

    print(f"{nums} numbers fall between {a} and {b}")
    print(f"{C[b]} - {C[a]} + {B[a]}")
    return


def sortAlgo(arr):
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    preprocessing(arr, start, end)


while True:
    if __name__ == "__main__":

        def remove(choice):
            return choice.replace(" ", "")

        element = 50

        # random .list of int
        array = [np.random.randint(0, high=50) for x in range(element)]
        # array = [x + 1 for x in range(element)]
        print(array)
        random.seed(time.time())
        random.shuffle(array)

        print("(Insertion) Sort, (Bubble) Sort, (Merge) Sort, (Heap) Sort,")
        print("(Quick) Sort, (Radix) Sort, (Bucket) Sort, (Counting) Sort,")
        print("(mod_quick) Sort, (int_query) Algorithm")
        print("OR (Quit)")
        choice_msg = "What algorithm do you want to use?: "
        choice = input(choice_msg)

        # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        # filename = (
        #     askopenfilename()
        # )  # show an "Open" dialog box and return the path to the selected file

        # with open(filename, "r") as fptr:
        #     array = fptr.read()

        # with open("D://data.txt", "r") as fptr:
        #     array = fptr.read()

        # list_of_string = list(array.split())
        # list_of_num = list(map(int, list_of_string))

        # # Check if there is a non-integer value in array
        # if not all(str(s).strip("-").isdigit() for s in list_of_num):
        #     print("Non integer value found in data, program exiting")
        #     array = None
        #     sys.exit(-1)
        # else:
        #     array = list_of_num

        # element = len(array)
        # print(f"Array: {array}")

        if remove(choice.lower()) == "insertion":
            title = "Insertion sort"
            space = "Space complexity: Θ(1)"
            time_comp = "Worst case time complexity: Θ(N^2)"
            animation_generator = Insertionsort(array)
            print("\n")
        elif remove(choice.lower()) == "bubble":
            title = "Bubble sort"
            space = "Space complexity: Θ(1)"
            time_comp = "Worst-case time complexity: O(N^2)"
            animation_generator = Bubblesort(array)
            print("\n")
        elif remove(choice.lower()) == "merge":
            title = "Merge sort"
            space = "Space complexity: Θ(N) (auxillary)"
            time_comp = "Worst case time complexity: Θ(N log N)"
            animation_generator = Mergesort(array, 0, element - 1)
            print("\n")
        elif remove(choice.lower()) == "heap":
            title = "Heap sort"
            space = "Space complexity: Θ(1)"
            time_comp = "Worst case time complexity: Θ(N log N)"
            animation_generator = Heapsort(array)
            print("\n")
        elif remove(choice.lower()) == "quick":
            title = "Quick sort"
            space = "Space complexity: Θ(N)"
            time_comp = "Worst case time complexity: Θ(N^2)"
            animation_generator = Quicksort(array, 0, element - 1)
            print("\n")
        elif remove(choice.lower()) == "radix":
            title = "Radix Sort"
            space = "Space complexity: O(N + K)"
            time_comp = "Worst case time complexity: Θ(n * k)"
            animation_generator = Radixsort(array)
            print("\n")
        elif remove(choice.lower()) == "bucket":
            title = "Bucket Sort"
            space = "Space complexity: Θ(N + K)"
            time_comp = "Worst case time complexity: Θ(N^2)"
            animation_generator = Bucketsort(array)
            print("\n")
        elif remove(choice.lower()) == "counting":
            title = "Counting Sort"
            space = "Space complexity: Θ(N + K)"
            time_comp = "Worst case time complexity: Θ(N + K)"
            animation_generator = Countingsort(array)
            print("\n")
        elif remove(choice.lower()) == "mod_quick":
            title = "Modified Quick Sort"
            # TODO: Add modified quick sort method
            time_comp = "Worst case time complexity: Θ(N^2)"
            space = ""
            animation_generator = quick_insertion_sort(array, 0, len(array) - 1)
            print("\n")
        elif remove(choice.lower()) == "int_query":
            title = "Integer Array Query"
            # TODO: Add integer query method
            time_comp = "Worst case time complexity: Θ(N + K)"
            space = "Space complexity: Θ(N + K)"
            animation_generator = Countingsort(array)
            print("\n")
        elif remove(choice.lower()) == "quit":
            break
        else:
            print("That is not a choice\n")
            continue

        if remove(choice.lower()) == "int_query":
            sortAlgo(array)

        # mm_per_inch = 25.4
        # root = tkinter.Tk()
        # width = (root.winfo_screenwidth() / mm_per_inch) - 2
        # height = (root.winfo_screenheight() / mm_per_inch) - 2

        # figure, axis = plt.subplots(figsize=(width, height), dpi=300)
        figure, axis = plt.subplots(figsize=(16, 9))
        # figure.set_tight_layout(0.4)

        # axis.set_title(title + "\n" + time_comp + "\n" + space)
        axis.set_title(title)

        bar_rects = axis.bar(range(len(array)), array, align="edge", color="grey")

        axis.set_xlim(0, element)
        axis.set_ylim(0, 1.2 * max(array))

        text = axis.text(0.02, 0.95, "", transform=axis.transAxes)
        info_time = axis.text(0.02, 0.90, f"{time_comp}", transform=axis.transAxes)
        info_space = axis.text(0.02, 0.85, f"{space}", transform=axis.transAxes)

        iteration = [0]

        def update_figure(array, rects, iteration):
            check = 0
            prev_value = 0
            for rect, val in zip(rects, array):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text(f"Number of operations: {iteration[0]}")

        anim = animation.FuncAnimation(
            figure,
            func=update_figure,
            fargs=(bar_rects, iteration),
            frames=animation_generator,
            interval=1,
            repeat=False,
        )

        plt.show()
