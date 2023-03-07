def insertion_sort(arr, low, n):
    # print("Performing insertion sort...")
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val


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


def quick_insertion(arr, low, high, limit):
    while low < high:

        if high - low + 1 < limit:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            if pivot - low < high - pivot:
                quick_insertion(arr, low, pivot - 1, limit)
                low = pivot + 1
            else:
                quick_insertion(arr, pivot + 1, high, limit)
                high = pivot - 1
