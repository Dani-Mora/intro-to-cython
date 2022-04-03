from typing import List


def quicksort(values: List[int]) -> List[int]:
    result = values.copy()
    _quicksort(result, 0, len(result) - 1)
    return result


def partition(values: List[int], left: int, right: int) -> int:

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


def swap(values: List[int], idx1: int, idx2: int) -> None:
    values[idx1], values[idx2] = values[idx2], values[idx1]


def _quicksort(values: List[int], left: int, right: int) -> None:
    if left > right:
        return

    part_idx = partition(values, left, right)
    _quicksort(values, left, part_idx - 1)
    _quicksort(values, part_idx + 1, right)
