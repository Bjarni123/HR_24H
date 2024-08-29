nr = int(input())

nr1 = nr ** 2
nr2 = (nr + 1) ** 2

print(f"Primes in the range {nr1} and {nr2} are:")

for x in range(nr1, nr2 + 1):
    if x > 1:
        isPrime = True
        for y in range(2, nr2 // 2 + 1):
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            print(x)