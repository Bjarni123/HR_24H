n = int(input("Enter a positive integer: "))

counter = 0
result = 1
while counter != n:
    counter += 1
    result *= counter

print(str(n) + "! is", result)