def sort(collection):

    l = len(collection)

    for i in range(l-1):

        for j in range(l-1-i):

            if collection[j] > collection[j+1]:

                collection[j], collection[j+1] = collection[j+1], collection[j]

    return collection

