number = int(input("Enter an integer: "))

counter = 0
while True:
    counter += 1
    square = counter ** 2
    if square > number:
        break
    print(square)
