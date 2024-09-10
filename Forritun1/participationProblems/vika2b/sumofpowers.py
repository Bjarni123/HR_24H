k = int(input())
n = int(input())

sum = 0

for i in range(n):
    x = int(input())
    sum += k ** x

print(sum)