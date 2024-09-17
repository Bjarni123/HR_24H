n = int(input())
prevNum1 = 0
prevNum2 = 1
prevNum3 = 0
number = 0

for x in range(n):
    number = number + prevNum1 + prevNum2
    print(number)
    prevNum1, prevNum2, prevNum3 = prevNum2, prevNum3, number

