# A sort is said to be stable
# if it does not change the order of equal elements

def merge(A:list, B:list):
    """ for Merge sorting var1 """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while i < len(B):
        C[k] = B[i]
        k += 1
        n += 1
    return C

def merge_sort(A:list):
    """ recursive """
    if len(A) <= 1:
        return
    middle = len(A) // 2
    left_part = [A[i] for i in range(middle)]
    right_part = [A[i] for i in range(middle, len(A))]
    merge_sort(left_part)
    merge_sort(right_part)
    C = merge(left_part, right_part)
    for i in range(len(A)):  # A = C[:]
        A[i] = C[i]
