budget = int(input())

budget -= int(input())
budget -= int(input())
budget -= int(input())

if budget < 0:
    print("Budget is insufficient.")
else:
    print("Budget is sufficient.")