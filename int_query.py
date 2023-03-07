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
    # nums = 0

    # nums = int(input("Enter number of entries: "))

    # arr = [0] * nums

    # for count in range(nums):
    #     arr[count] = int(input(f"Input integer number {count + 1}:"))

    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))

    preprocessing(arr, start, end)
