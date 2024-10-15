the_set = set()

for x in range(10):
    the_number = int(input())
    the_set.add(the_number % 42)

print(len(the_set))