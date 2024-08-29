nr = int(input())
print(nr)

while nr != 1:
    if nr % 2 == 0:
        nr = nr / 2
    else:
        nr = (3 * nr) + 1
    print(int(nr))