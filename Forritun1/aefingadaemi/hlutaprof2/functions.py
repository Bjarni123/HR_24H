def get_input_list(n):
    if n <= 0:
        return None
    else:
        return [int(input('insert number: ')) for x in range(n)]

def get_average_list(the_list):
    print(the_list)
    return sum(the_list) / len(the_list)

def triple_values(the_list):
    return [3*x for x in the_list]

thingy = get_input_list(0)
print(thingy)
avg = get_average_list(thingy)
print(avg)
three = triple_values(thingy)
print(three)