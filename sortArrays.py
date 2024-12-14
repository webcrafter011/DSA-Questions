def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
        
    return merged

array = [2, 2, 2, 2, 1, 0, 1, 2, 2, 0, 1, 0, 2, 0, 1, 0, 1, 1, 1, 0, 
 1, 1, 1, 1, 0, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 
 2, 2, 2, 2, 2, 0, 0, 0, 2, 0, 1, 0, 2, 2, 1, 0, 1, 2, 2, 1, 
 0, 1, 0, 1, 2, 1, 0, 1, 0, 2, 2, 0, 2, 0, 0, 2, 1, 1, 0, 1, 
 1, 1, 2, 1, 0, 2, 1, 1, 0, 2, 1, 1, 1, 2, 0, 1, 1, 2, 2, 1]

print(merge_sort(array))