import sys

def multikeyquicksort(seq, cmpindex=0):
    if not seq:
        return []
    pivot = seq[0]['str']
    left = []
    mid = []
    right = []

    for i in range(1, len(seq)):
        #print(seq[i])
        if seq[i]['str'][cmpindex] < pivot[cmpindex]:
            left.append(seq[i])
        elif seq[i]['str'][cmpindex] == pivot[cmpindex]:
            mid.append(seq[i])
        else:
            right.append(seq[i])
    mid.append(seq[0])

    if not pivot[cmpindex] == '$' and not len(mid) < 2:
        mid = multikeyquicksort(mid, cmpindex+1)
    
    left = multikeyquicksort(left, cmpindex)
    right = multikeyquicksort(right, cmpindex)

    return left + mid + right

f = open(sys.argv[1])
string = f.read() + '$'
strings = [{'str': string[i:], 'index': i} for i in range(len(string))]
#print('ok!')

#for suffix in strings:
    #print(suffix)

array = []

for suffix in multikeyquicksort(strings):
    #print(suffix['str'])
    #print(suffix['index'])
    array.append(suffix['index'])

print(array)


