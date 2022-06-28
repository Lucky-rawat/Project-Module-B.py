def QuickSort(arr):
    elements = len(arr)

    if elements < 2:
        return arr

    pos = 0

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            pos += 1
            temp = arr[i]
            arr[i] = arr[pos]
            arr[pos] = temp

    temp = arr[0]
    arr[0] = arr[pos]
    arr[pos] = temp

    left = QuickSort(arr[0:pos])
    right = QuickSort(arr[pos + 1:elements])

    arr = left + [arr[pos]] + right

    return arr


array_to_be_sorted = [4, 2, 7, 3, 1, 6]
print("Original Array: ", array_to_be_sorted)
print("Sorted Array: ", QuickSort(array_to_be_sorted))