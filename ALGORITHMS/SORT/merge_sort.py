def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=0 #left arr
        j=0 #right arr
        k=0 #merged arr

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            
            else:
                arr[k] = right_arr[j]
                j+=1

            k+=1

        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1


        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

        return arr




arr = [1,3,6,11,87,90,44,23,54,22,11,6,7]
print(merge_sort(arr))