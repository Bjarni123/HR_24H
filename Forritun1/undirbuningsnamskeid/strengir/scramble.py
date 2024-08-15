strengur = input("Enter in sentence: ")

for word in strengur.split():
    print(word[-1] + word[1: -1] + word[0], end=" ")
print()