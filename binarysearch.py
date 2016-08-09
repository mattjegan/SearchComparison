
def binary_search(array, target):
    first = 0
    last = len(array) - 1
    comparisons = 0

    while first <= last:
        comparisons += 1
        midpoint = (first + last) // 2
        if array[midpoint] == target:
            return (midpoint, comparisons)
        elif array[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return (first, comparisons)