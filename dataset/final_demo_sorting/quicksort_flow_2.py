def _partition(array, lo, hi):
    pivot = array[hi]
    i = lo - 1
    for j in range(lo, hi):
        if array[j] < pivot:
                i += 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[hi]
    array[hi] = temp
    return i + 1

def _quicksort(array, lo, hi):
    if lo < hi:
            p = _partition(array, lo, hi)
            _quicksort(array, lo, p - 1)
            _quicksort(array, p + 1, hi)
    return array

def quicksort(array):
    return _quicksort(array, 0, len(array) - 1)

arr=[10, 20 , 30 , -8, -2]
n=len(arr)
quicksort(arr) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])