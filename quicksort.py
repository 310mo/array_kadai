def quicksort(seq):
    if not seq:
        return []
    pivot = seq.pop(0)
    left = []
    right = []
    for i in range(len(seq)):
        if seq[i] < pivot:
            left.append(seq[i])
        else:
            right.append(seq[i])
    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right

seq = [4, 2, 3, 6 ,9, 1, 10, 5, 7]

print(quicksort(seq))