def Bubblesort(array):
    n = len(array)

    if n == 1:
        return

    optimized = True

    for i in range(n - 1):
        if not optimized:
            break
        optimized = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                optimized = True
