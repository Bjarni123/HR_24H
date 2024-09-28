how_many = int(input())

listi = []
for x in range(how_many):
    listi.append(int(input()))

for number in listi[::-1]:
    print(number)