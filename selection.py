def selectionSort(arr, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
 

arr = [5, 7, 56, 9, 12, 2, 3]
size = len(arr)
selectionSort(arr, size)
print(arr)