def selection_sort(list_a):
    length = range(0, len(list_a)-1)

    for i in length:
        min_index = i
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_index]:
                min_index = j
            
        if min_index != i:
            list_a[i], list_a[min_index] = list_a[min_index], list_a[i]
    
    return list_a

print(selection_sort([5, 7, 9, 1, 3, 2, 4, 6, 8]))