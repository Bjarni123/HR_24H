print("You need something doubled? (Y)es?")
answer = input()

while answer.upper() == "Y":
    print("All right, then. Give me a number, and I'll double it for ya:")
    nr = float(input())
    print('{:.6f}'.format(nr * 2))
    print("You need something else doubled? (Y)es?")
    answer = input()
