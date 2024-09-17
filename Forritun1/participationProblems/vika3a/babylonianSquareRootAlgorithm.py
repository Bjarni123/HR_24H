n = int(input())
g = int(input())
t = float(input())
prevG = 0


counter = 0
print(prevG - g)
while -t < (prevG - g) > t:
    print(prevG - g)
    counter += 1
    g = (((n/g)+g) / 2)
    prevG = g

print(g)
print(counter)
