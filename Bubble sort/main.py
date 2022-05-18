def bubble(list_a):
    length = len(list_a)
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, length - 1):
            if list_a[i] > list_a[i + 1]:
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
                sorted = False
    return list_a

print(bubble([5, 7, 9, 1, 3, 2, 4, 6, 8]))