def bubble_sort(a):
    for i in range(len(a)):
        for j in  range(len(a)):
            if(a[j] > a[i]):
                a[i], a[j] = a[j], a[i]
    return a


