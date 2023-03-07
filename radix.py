def RadixCountingsort(array, exp1, element):
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

    i = 0
    for i in range(0, len(array)):
        array[i] = output_array[i]


def Radixsort(array):
    max1 = max(array)
    exp = 1

    while max1 / exp > 0:
        RadixCountingsort(array, exp, len(array))
        exp = exp * 10
