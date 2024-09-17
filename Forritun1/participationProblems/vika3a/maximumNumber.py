number = 0
max = 0
while number >= 0:
    number = int(input())
    if max < number:
        max = number

print(max)