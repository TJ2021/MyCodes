def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        already_sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                already_sorted = False

        if already_sorted == True:
            break
    return arr

arr = [15,2,90,34,23,12]
print(bubble_sort(arr))
