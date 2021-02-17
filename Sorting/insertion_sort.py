def insertion_sort(arr):
    for i in range(1,len(arr)):
        print(i)
        j = i-1
        key_item = arr[i]
        while j>= 0 and arr[j] > key_item:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key_item
    return arr

arr = [34,2,56,43,80,6,1]
print(insertion_sort(arr))
            
    
    
    
