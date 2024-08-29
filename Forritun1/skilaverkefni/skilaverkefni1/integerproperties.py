number = input()

while not (number == 'q' or number == 'Q'):
    number = int(number)
    divisorscount = 2
    for d in range(2, number // 2 + 1):
        if number % d == 0:
            divisorscount += 1
    
    if divisorscount < 10:
        print('no')
    else:
        print('yes')

    number = input()


number = int(input())

upperlimit = 99
lowerlimit = 10

for power in range(2, 4):
    if number < upperlimit:
        upperlimit = number

    for element in range(lowerlimit, upperlimit + 1):
        summatalna = 0
        for singlenumber in str(element):
            summatalna += int(singlenumber)
        if summatalna ** power == element:
            print(element)

    lowerlimit = 100
    upperlimit = 1000

        



