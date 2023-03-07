# Script to test and time function executions and result average running time of algorithms
from time import process_time
from time import perf_counter
from time import process_time_ns
import numpy as np
import random
import time

from bubble import Bubblesort
from bucket import Bucketsort
from counting import Countingsort
from heap import Heapsort
from insertion import Insertionsort
from merge import Mergesort
from quick import Quicksort
from radix import Radixsort
from mod_quicksort import quick_insertion

# from int_query import sortAlgo

algorithms = Bubblesort

algorithms = [
    Bubblesort,
    Bucketsort,
    Countingsort,
    Heapsort,
    Insertionsort,
    Mergesort,
    Quicksort,
    Radixsort,
    quick_insertion
    # sortAlgo,
]


def generate_data(element=100):
    # element = int(input("Enter the number of elements for the array: "))
    # element = 1000

    with open("results.txt", "a") as writer:
        writer.write(str(f"Number of elements in array: {element}") + "\r\n")

    # random list of int
    array = [np.random.randint(0, high=1000) for x in range(element)]
    np_array = np.array(array)

    # array = [x + 1 for x in range(element)]
    random.seed(time.time())
    random.shuffle(array)

    return np_array


def write_to_file(algoName, elapsed_time, *args):
    if args:
        with open("results.txt", "a") as writer:
            writer.write("\r\n")
    else:
        with open("results.txt", "a") as writer:
            writer.write(
                str(f"Algorithm {algoName} sort: Execution time: {elapsed_time}")
                + "\r\n"
            )

    print(f"{algoName} sort done")


if __name__ == "__main__":

    # results = np.ndarray((9, 10), dtype="int")
    # averages = np.ndarray((9, 1), dtype="int")

    print("Starting execution...")

    iter_count = 1

    # initial = perf_counter()
    # data = generate_data(1000)
    # final = perf_counter() - initial

    # print(str(final))
    sizes = list(range(500, 5100, 500))

    for run in sizes:
        data = generate_data(run)
        high = len(data) - 1
        print(f"Iteration {iter_count}")

        data_copy = data.copy()
        initial_time = perf_counter()
        Bubblesort(data_copy)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Bubble", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Bucketsort(data_copy)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Bucket", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Countingsort(data_copy)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Counting", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Heapsort(data_copy)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Heap", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Insertionsort(data_copy)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Insertion", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Mergesort(data_copy, 0, high)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Merge", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Quicksort(data_copy, 0, high)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Quick", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        Radixsort(data_copy)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Radix", elapsed_time)

        data_copy = data.copy()
        initial_time = perf_counter()
        quick_insertion(data_copy, 0, high)
        elapsed_time = perf_counter() - initial_time
        write_to_file("Modified Quick", elapsed_time)

        write_to_file("Finished", 0, "exit")
        iter_count += 1

    # for algo in range(len(algorithms) - 1):

    #     data_copy = data_copy

    # initial_time = process_time_ns()
    # # algorithms[algo](data_copy, 0, len(data_copy) - 1)
    # elapsed_time = process_time_ns() - initial_time

    #     # print(f"{algorithms[algo]} iteration {run + 1} ran in {elapsed_time} ns")
    #     results[algo][run] = elapsed_time
    # results[algo][run] = int(str(algo) + str(run))

    # print(results)

    # for i in range(10):
    #     average[i] = np.average(results[i][::])
