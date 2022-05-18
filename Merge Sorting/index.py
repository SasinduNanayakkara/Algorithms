def mergeSort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2] # add the beginning to middle of the array
        right = arr[len(arr) // 2:] # add the middle to the end of the array

        # recursively call mergeSort on the left and right arrays
        mergeSort(left)
        mergeSort(right)

        #merge the two arrays
        i = 0 # index for left array
        j = 0 # index for right array
        k = 0 # index for merged array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

testArray = [0, 9, 3, 8, 2, 7, 5]
mergeSort(testArray)
print(testArray)