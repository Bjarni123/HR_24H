a = bool(int(input()))
b = bool(int(input()))
c = bool(int(input()))

and1 = (a and (not b))
and2 = ((not a) and c)

d = and1 or and2

if d:
    print(1)
else:
    print(0)