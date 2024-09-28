days_amount = int(input())
days_list = list(map(int, input().split()))

highest = days_list[0]
lowest = days_list[0]
for day in days_list:
    if day < lowest:
        lowest = day
    elif day > highest:
        highest = day

print(highest, lowest)