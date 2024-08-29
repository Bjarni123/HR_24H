nr = int(input())

isPrime = True

if nr > 1:
    for x in range(2, nr //2 + 1):
        if nr % x == 0:
            isPrime = False
            break
else:
    isPrime = False

if isPrime:
    print("prime")
else:
    print("not prime")