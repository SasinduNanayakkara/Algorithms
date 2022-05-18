import heapq

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 -1, -1, -1):
        max_heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heap(arr, i, 0)

def max_heap(arr, n, parent_index):
    largest = parent_index
    left_index = 2 * parent_index + 1
    right_index = 2 * parent_index + 2

    if left_index < n and arr[left_index] > arr[largest]:
        largest = left_index

    if right_index < n and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != parent_index:
        arr[largest], arr[parent_index] = arr[parent_index], arr[largest]
        max_heap(arr, n, largest)
        

arr = [10, 45, 23, 1, 67, 2]
heapsort(arr)
print(arr)