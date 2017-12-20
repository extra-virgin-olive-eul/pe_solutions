from itertools import permutations

p = permutations('0123456789')
for i in range(0, 1000000):
    perm = next(p)

print(''.join(perm))
