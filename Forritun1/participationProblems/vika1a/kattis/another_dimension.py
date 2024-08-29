import math

d = float(input())
r = d / 2

Volume = (4/3) * math.pi * (r ** 3)

halfVolume = Volume / 2

print('{:0.15f}'.format(halfVolume))