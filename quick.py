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

        Quicksort(array, low, pi - 1)
        Quicksort(array, pi + 1, high)
        return array
