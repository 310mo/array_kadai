import sys

f = open(sys.argv[1])

file = f.read()

result = ''

for s in file:
    if ord(s)<=127:
        result += s

print(result)