the_list = []
list_of_tuples = []

the_input = ''

while the_input.lower() != 'q':
    the_input = input()

    if the_input == 'q':
        continue

    the_list.append(the_input)
    list_of_tuples.append(tuple(the_input.split()))

print(the_list)
print(list_of_tuples)
