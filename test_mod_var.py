# Script to test and time function executions and result average running time of algorithms
from time import process_time
from time import perf_counter
from time import process_time_ns
import numpy as np
import random
import time

from mod_quicksort_variable_insert import quick_insertion


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


# def write_to_file(algoName, elapsed_time, *args):
#     if args[0] == "exit":
#         with open("mod_quick_sort_var.txt", "a") as writer:
#             writer.write("\r\n")
#     else:
#         with open("mod_quick_sort_var.txt", "a") as writer:
#             writer.write(
#                 str(
#                     f"""Algorithm {algoName} sort: Execution time: {elapsed_time},
#                     Insertion sort limit: {args[0]}, Data size: {args[1]}"""
#                 )
#                 + "\r\n"
#             )

#     print(f"{algoName} sort done")


def write_to_file(algoName, elapsed_time, *args):
    if args[0] == "exit":
        with open("mod_quick_sort_var.txt", "a") as writer:
            writer.write("\r\n")
    else:
        with open("mod_quick_sort_var.txt", "a") as writer:
            writer.write(
                str(
                    f"""Algorithm {algoName} sort: Execution time: {elapsed_time},Insertion sort limit: {args[0]}, Data size: {args[1]}"""
                )
                + "\r\n"
            )

    print(f"{algoName} sort done")


if __name__ == "__main__":

    # results = np.ndarray((9, 10), dtype="int")
    # averages = np.ndarray((9, 1), dtype="int")

    print("Starting execution...")

    iter_count = 0

    # initial = perf_counter()
    # data = generate_data(1000)
    # final = perf_counter() - initial

    # print(str(final))
    sizes = list(range(100, 1001, 100))
    # limits = [8, 32, 64, 1024]
    limits = [10, 20, 30, 40, 50, 60]

    for limit in limits:
        for run in sizes:
            # print(f"limit: {limit}, size: {run}")
            data = generate_data(run)
            high = len(data) - 1
            print(f"Iteration {iter_count}")

            data_copy = data.copy()
            initial_time = perf_counter()
            quick_insertion(data_copy, 0, high, limits[iter_count])
            elapsed_time = perf_counter() - initial_time
            write_to_file("Modified quick", elapsed_time, limits[iter_count], run)

            write_to_file("Finished", 0, "exit")
        iter_count += 1
