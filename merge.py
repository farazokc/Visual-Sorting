def Mergesort(array, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    Mergesort(array, start, mid)
    Mergesort(array, mid + 1, end)
    merge(array, start, mid, end)
    return array


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
