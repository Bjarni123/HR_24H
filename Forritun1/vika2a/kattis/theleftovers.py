playercount = 0

while playercount < 2:
    playercount = int(input())

sum = 0

for x in range(playercount):
    sum += int(input())

remainder = sum % playercount

print(f"The sum of all contributions is {sum} When {sum} is divided by {playercount}, the remainder is {remainder} Player {remainder} is the winner!")