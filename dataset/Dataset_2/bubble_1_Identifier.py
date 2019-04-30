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


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    u_input = raw_input('Enter numbers:').strip()
    LIST = [int(i) for i in u_input.split(',')]
    print(*sort(LIST), sep=',') 
    