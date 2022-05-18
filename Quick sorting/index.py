def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    itemsGreater = []
    itemsLower = []

    for item in sequence:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)
    
    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)


print(quickSort([0, 9, 3, 8, 2, 7, 5]))