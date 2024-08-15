numbers_amount = int(input("How many numbers do you want to type in?: "))

minimum = 99999999999999999
maximum = -9999999999999999
summa = 0

for x in range(numbers_amount):
    number = int(input("Enter in a number: "))
    summa += number
    if minimum > number:
        minimum = number
    if maximum < number:
        maximum = number

print("The max number is {}, the min number is {} and the average is {}".format(maximum, minimum, summa/numbers_amount))