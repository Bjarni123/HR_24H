sentence = input("Enter in a sentece: ")

digits = 0
uppercase = 0
lowercase = 0

for x in sentence:
    if x.isalpha():
        if x.islower():
            lowercase += 1
        else:
            uppercase += 1
    elif x.isnumeric():
        digits += 1

print(f"The input has {digits} digits and {uppercase + lowercase} alphabetic characters, where {uppercase} are upper case and {lowercase} are lower case")