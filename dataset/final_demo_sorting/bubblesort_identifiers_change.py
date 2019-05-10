# Python program for implementation of Bubble Sort 
  
def bubble_sort(a): 
    length = len(a) 
  
    # Traverse through all array elements 
    for i in range(length): 
  
        # Last i elements are already in place 
        for j in range(0, length-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if a[j] > a[j+1] : 
                a[j], a[j+1] = a[j+1], a[j] 
  
# Driver code to test above 
a = [64, 34, 25, 12, 22, 11, 90] 
  
bubble_sort(a) 
  
print("Sorted aay is:") 
for ind in range(len(a)): 
    print ("%d" %a[ind])