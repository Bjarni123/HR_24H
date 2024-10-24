value_count = int(input("How many pairs? "))
the_dict = dict()
for x in range(value_count):
    the_key = input("What is the ID? ")
    the_value = input("What is the name? ")
    the_dict[the_key] = the_value

option = 0
while option != 'q':
    option = input('What id to look up (q to quit)? ')
    try:
        print(the_dict[option])
    except:
        pass

print("Quiting...")