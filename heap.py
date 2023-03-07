def heapify(array, element, i):
    high = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < element and array[i] < array[left]:
        high = left
    if right < element and array[high] < array[right]:
        high = right

    array[i], array[high] = array[high], array[i]
    if high != i:
        # array[i], array[high] = array[high], array[i]
        heapify(array, element, high)


def Heapsort(array):
    element = len(array)
    for i in range(element // 2 - 1, -1, -1):
        heapify(array, element, i)

    for i in range(element - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
