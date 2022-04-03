cpdef int[:] quicksort(int[:] values):
    cdef int[:] result
    cdef int n
    result = values.copy()
    n = len(result)
    _quicksort(result, 0, n - 1)
    return result



cpdef int partition(int[:] values, int left, int right):
    cdef int pivot_idx, pivot_value, i, part_idx

    pivot_idx = (right + left) // 2
    pivot_value = values[pivot_idx]

    swap(values, pivot_idx, right)

    part_idx = left
    for i in range(left, right):
        if values[i] <= pivot_value:
            swap(values, part_idx, i)
            part_idx += 1

    swap(values, part_idx, right)
    return part_idx


cpdef void swap(int[:] values, int idx1, int idx2):
    values[idx1], values[idx2] = values[idx2], values[idx1]


cpdef void _quicksort(int[:] values, int left, int right):
    cdef int part_idx
    if left > right:
        return

    part_idx = partition(values, left, right)
    _quicksort(values, left, part_idx - 1)
    _quicksort(values, part_idx + 1, right)
