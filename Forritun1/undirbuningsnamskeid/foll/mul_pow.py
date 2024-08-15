def multiply(a, b):
    summa = 0
    for x in range(b):
        summa += a
    return summa

def power(a, b):
    summa = 1
    for x in range(b):
        summa = multiply(summa, a)
    return summa

fyrsta_numer = int(input("Enter in a number: "))
seinna_numer = int(input("Enter in a second number: "))

print(multiply(fyrsta_numer, seinna_numer))
print(power(fyrsta_numer, seinna_numer))