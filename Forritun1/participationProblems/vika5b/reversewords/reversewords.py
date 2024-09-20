filename = input()

with open(f'/src/{filename}', 'r') as file:
    for line in file:
        for word in line.split():
            print(word[::-1], end=' ')
        print()