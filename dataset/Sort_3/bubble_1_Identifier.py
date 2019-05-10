def sort(LIST):
    l = len(LIST)
    for i in range(l-1):
        flag = False
        for j in range(l-1-i):
            if LIST[j] > LIST[j+1]:
                flag = True
                LIST[j], LIST[j+1] = LIST[j+1], LIST[j]
        if not flag: break  # Stop iteration if the LIST is sorted.
    return LIST