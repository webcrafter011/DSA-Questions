array = [3, 1, 3, 4, 2]

def duplicateAndMissing(array):
    array.sort()
    n = len(array)
    duplicate = -1
    missing = -1

    for i in range(n - 1):
        if array[i] == array[i + 1]:
            duplicate = array[i]
        elif array[i + 1] - array[i] > 1:
            missing = array[i] + 1

    # Check for the missing number at the boundaries
    if array[0] != 1:
        missing = 1
    elif array[-1] != n:
        missing = n
    
    return [duplicate, missing]

print(duplicateAndMissing(array))
