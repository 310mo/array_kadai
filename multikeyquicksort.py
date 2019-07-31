def multikeyquicksort(seq, cmpindex=0):
    if not seq:
        return []
    pivot = seq[0]
    left = []
    mid = []
    right = []

    for i in range(1, len(seq)):
        if seq[i][cmpindex] < pivot[cmpindex]:
            left.append(seq[i])
        elif seq[i][cmpindex] == pivot[cmpindex]:
            mid.append(seq[i])
        else:
            right.append(seq[i])
    mid.append(pivot)

    if not pivot[cmpindex] == '$' and not len(mid) < 2:
        mid = multikeyquicksort(mid, cmpindex+1)
    
    left = multikeyquicksort(left, cmpindex)
    right = multikeyquicksort(right, cmpindex)

    return left + mid + right

string = 'mississippi$'
strings = [string[i:] for i in range(len(string)-1)]
index = []
for suffix in strings:
    print(suffix)
for i in range(len(strings)):
    index.append(i)

for suffix in multikeyquicksort(strings):
    print(suffix)
