def selection_sort(arr):
    i= 0
    min = 0

    while i < len(arr):

        min=i 
        j = i+1

        while j < len(arr):

            if arr[j] < arr[min]:
                min = j

            j+=1

        placeholder = 0
        placeholder = arr[i]
        arr[i] = arr[min]
        arr[min] = placeholder

        i+=1

    return arr

print(selection_sort([2,1,9,2,5,4]))

            
