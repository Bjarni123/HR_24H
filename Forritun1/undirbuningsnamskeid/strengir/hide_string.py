strengur = input("Enter a string to hide: ")
print("Your string:", strengur)

while strengur != len(strengur) * "*":
    hide_character = input("Enter a character to hide: ")
    if len(hide_character) != 1:
        print("Only one character at a time!")
    else:
        strengur = strengur.replace(hide_character, "*")
    print("Your string:", strengur)