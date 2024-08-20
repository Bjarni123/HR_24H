strengur = ""
the_input = ""
while the_input != "done":
    the_input = str(input("Enter a single character to add to string: "))
    if the_input == "done":
        break
    elif len(the_input) != 1:
        print("Input must be a single character")
    else:
        strengur += the_input

print(strengur)