strengur = input("Enter in a string: ")
substring = input("What substring do you want to check?: ")

if substring in strengur:
    print(substring, "is a substring of", strengur)
else:
    print("There is no", substring, "in", strengur)