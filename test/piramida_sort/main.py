def heapify(arr, n, i):  # i корневое значение, n - размер пирамиды
    largest = i  # наибольшее значение - корневое
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корневое значение, если оно меньше наследника
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # меняем

        # Кучерявим корневое значение.
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)


arr = [9, 5, 3, 5, 6, 1, 18, 4, 2, 77,9]
heapSort(arr)
n = len(arr)

for i in range(n):
    print(arr[i])