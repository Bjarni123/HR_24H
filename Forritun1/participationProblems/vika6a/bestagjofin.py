number_of_friends = int(input())
best_one = ["", 0]

for x in range(number_of_friends):
    name, rating = input().split()
    if int(rating) > best_one[1]:
        best_one = [name, int(rating)]

print(best_one[0])