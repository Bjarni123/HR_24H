number = int(input("Input a number: "))

for x in range(2, number // 2 + 1):
    if number % x == 0:
        print(x)