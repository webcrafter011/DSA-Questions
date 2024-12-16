array = [5, 3, 2, 1, 4]


def merge_sort(array):
    if len(array) <= 1:
        return array, 0

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_sorted, left_inversions = merge_sort(left_half)
    right_sorted, right_inversions = merge_sort(right_half)

    merged, split_inversions = merge(left_sorted, right_sorted)

    # Total inversions = inversions in left part + inversions in right part + split inversions
    total_inversions = left_inversions + right_inversions + split_inversions

    return merged, total_inversions


def merge(left, right):
    i = j = 0
    merged = []
    count = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            count += len(left) - i
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, count


sorted_array, inversion_count = merge_sort(array)
print(inversion_count)