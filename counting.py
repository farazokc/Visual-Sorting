def Countingsort(array):
    element = len(array)
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
    for i in range(0, element):
        array[i] = out_array[i]
