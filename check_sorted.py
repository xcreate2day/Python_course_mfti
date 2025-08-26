def check_sorted(A:list, asc=True):
    """ check if is sorted O(n) """
    flag = True  # sorted
    s = 2 * int(asc) - 1  # True = 1
    for i in range(len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag


if __name__ == '__main__':
    print(check_sorted([1, 5, 8]))
    print(check_sorted([2, 5, 1]))
    print(check_sorted([1]))
    print(check_sorted([1, 1, 1]))
    print(check_sorted([7, 5, 1], False))
