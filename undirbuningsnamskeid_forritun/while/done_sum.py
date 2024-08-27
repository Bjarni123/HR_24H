the_sum = 0
the_input = "0"

while the_input.lower() != "done":
    the_sum += int(the_input)
    the_input = input('Enter a number (or "done"): ')

print("The sum is", the_sum)