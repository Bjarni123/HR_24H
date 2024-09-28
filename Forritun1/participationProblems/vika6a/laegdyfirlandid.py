rows, column = map(int, input().split())
grid = {}

for rowIdx in range(1, rows + 1):
    grid[rowIdx] = {}
    rowinput = list(map(int, input().split()))
    for columnIdx in range(1, column + 1):
        grid[rowIdx][columnIdx] = rowinput[columnIdx-1]

isGood = False

for rowIdx in range(2, rows):
    for columnIdx in range(2, column):
        value = grid[rowIdx][columnIdx]
        if value < grid[rowIdx-1][columnIdx] and value < grid[rowIdx+1][columnIdx] and value < grid[rowIdx][columnIdx-1] and value < grid[rowIdx][columnIdx+1]:
            isGood = True
            break

if isGood:
    print("Jebb")
else:
    print("Neibb")