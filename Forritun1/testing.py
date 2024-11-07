from copy import deepcopy

zero = [[0] * 3] * 2
print(zero)
sorrow = zero[:]
print(zero, sorrow)
zorro = deepcopy(sorrow)
print(zero, sorrow, zorro)

zero[0][0] = 1
print(zero)
zero[0].pop()
zero[0].pop()

print(zero,'\n', sorrow, '\n', zorro)