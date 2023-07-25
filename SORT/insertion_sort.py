def insertion_sort(arr):

    for i in range(1,len(arr)):

        j=i
        
        while arr[j-1] > arr[j] and j != 0:
            placeholder = arr[j-1]  
            arr[j-1] = arr[j]
            arr[j] = placeholder
            j -=1

    return arr


arr=[1,3,6,2,8]


print(insertion_sort(arr))