def left_bound(A, key):
    left = -1
    right = len(A)
    while left - right > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while left - right > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right
 # O(log(n))
 # diff > 1?
