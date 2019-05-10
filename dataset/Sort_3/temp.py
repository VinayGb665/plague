def bsort(c):
    """Pure implementation of bubble sort algorithm in Python
    :param c: some mutable ordered c with heterogeneous
    comparable items inside
    :return: the same c ordered by ascending
    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    
    >>> bubble_sort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """
    l = len(c)
    for i in range(l-1):
        swapped = False
        for j in range(l-1-i):
            if c[j] > c[j+1]:
                swapped = True
                c[j], c[j+1] = c[j+1], c[j]
        if not swapped: break  # Stop iteration if the c is sorted.
    return c
