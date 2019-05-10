def quick_sort(collection):

    

    length = len(collection)

    if length <= 1:

        return collection

    else:

        pivot = collection[0]

        greater = [element for element in collection[1:] if element > pivot]

        lesser = [element for element in collection[1:] if element <= pivot]

        return quick_sort(lesser) + [pivot] + quick_sort(greater)

