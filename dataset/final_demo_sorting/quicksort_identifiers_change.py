# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(a,L,H): 
    i = ( L-1 )         # index of smaller element 
    pivot = a[H]     # pivot 
  
    for j in range(L , H): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   a[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            a[i],a[j] = a[j],a[i] 
  
    a[i+1],a[H] = a[H],a[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# a[] --> array to be sorted, 
# L  --> Starting index, 
# H  --> Ending index 
  
# Function to do Quick sort 
def quick_sort(a,L,H): 
    if L < H: 
  
        # pi is partitioning index, a[p] is now 
        # at right place 
        pi = partition(a,L,H) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(a, L, pi-1) 
        quick_sort(a, pi+1, H) 
  
# Driver code to test above 
a = [10, 7, 8, 9, 1, 5] 
n = len(a) 
quick_sort(a,0,n-1) 
print ("Sorted aay is:") 
for i in range(n): 
    print ("%d" %a[i]) 
  