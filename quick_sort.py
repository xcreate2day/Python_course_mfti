def hoar_sort(A):
    """ recursive """
    if len(a) <= 1:
        return  # None
    barrier = A[0]
    left_part = []
    right_part =[]
    middle = []
    for x in A:
        if x < barrier:
            left_part.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right_part.append(x)
    hoar_sort(left_part)
    hoar_sort(right_part)
    k = 0
    for x in left_part + middle + right_part:
        A[k] = x
        k += 1
