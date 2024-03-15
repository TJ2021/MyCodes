def quick_sort(A,start,end):
    if start < end:
        q = partition(A,start,end)
        quick_sort(A,start,q-1)
        quick_sort(A,q+1,end)

def partition(A,start,end):
    pivot = A[end]
    i = start - 1
    for j in range(start,end):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[end] = A[end], A[i+1]
    return i+1

if __name__ == '__main__':
    A = [3,6,2,9,1,8]
    quick_sort(A,0,len(A)-1)
    print(A)