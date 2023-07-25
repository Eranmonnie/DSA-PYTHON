def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left,  partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

    return arr

def partition(arr, left, right):
    i= left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i+=1
        
        while j > left and arr[j] >= pivot: 
            j-=1
            
        if i < j:
            placeholder = 0
            placeholder = arr[i]
            arr[i] = arr[j]
            arr[j] = placeholder

    if arr[i] > pivot:
        placeholder = 0
        placeholder = arr[i]
        arr[i] = arr[right]
        arr[right] = placeholder

    return i 





arr = [1,4,2,90,76,44,53,22,16,71]

print(quick_sort(arr, 0, len(arr)-1))
