def Kadane(arr, n):
    current_maximum = arr[0]
    maximum_so_far = arr[0]

    for i in range(1, n):
        current_maximum = max(arr[i], current_maximum + arr[i])
        maximum_so_far = max(maximum_so_far, current_maximum)

    return maximum_so_far


arr = [11, 22, 10, 5, -16]
print("Maximum sum is", Kadane(arr, len(arr)))