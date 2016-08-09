from binarysearch import binary_search

def galloping_search(array, target):

    if array[0] == target:
        return (0, 1)
    comparisons = 1

    # Stage 1 - Find the large index
    size = len(array)
    jump = 1
    cursor = 0
    while cursor < size and array[cursor] < target:
        comparisons += 1
        jump *= 2
        cursor += jump

    # Stage 2 - slice the array and run the binary search
    array = array[(cursor // 2):min(cursor, size) + 1]
    sub_search = binary_search(array, target)

    return ((cursor // 2) + sub_search[0] - 1, sub_search[1] + comparisons)