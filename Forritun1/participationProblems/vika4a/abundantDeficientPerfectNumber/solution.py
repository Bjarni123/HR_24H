def sum_of_divisors(n):
    sum = 0
    for x in range(1, n//2 + 1):
        if n % x == 0:
            sum += x
    return sum


def decide(n):
    sum = sum_of_divisors(n)
    if n > sum:
        return (f'{n} is deficient.')
    elif n < sum:
        return (f'{n} is abundant.')
    else:
        return (f'{n} is a perfect number.')
