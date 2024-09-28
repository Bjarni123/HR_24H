number1 = input()
number2 = input()

number1List = sorted([x for x in number1])
number2List = sorted([x for x in number2])


if number1List == number2List:
    print(f"The numbers {number1} and {number2} are permutations of each other.")
else:
    print(f"The numbers {number1} and {number2} are not permutations of each other.")